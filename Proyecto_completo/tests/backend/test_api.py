# pyright: reportMissingImports=false
"""
Tests de API para el backend de detección de tumores
"""
import pytest
from fastapi.testclient import TestClient  # type: ignore
import sys
import os

# Añadir path del backend
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'backend'))

from main import app  # type: ignore

client = TestClient(app)


class TestRootEndpoint:
    """Tests para el endpoint raíz"""
    
    def test_root_returns_200(self):
        """Verifica que el endpoint raíz responde correctamente"""
        response = client.get("/")
        assert response.status_code == 200
    
    def test_root_contains_title(self):
        """Verifica que la respuesta contiene el título"""
        response = client.get("/")
        data = response.json()
        assert "title" in data
        assert data["title"] == "API Detección de Tumores"
    
    def test_root_contains_version(self):
        """Verifica que la respuesta contiene la versión"""
        response = client.get("/")
        data = response.json()
        assert "version" in data
        assert data["version"] == "1.0.0"


class TestModelsEndpoint:
    """Tests para el endpoint /models"""
    
    def test_models_returns_200(self):
        """Verifica que el endpoint de modelos responde correctamente"""
        response = client.get("/models")
        assert response.status_code == 200
    
    def test_models_returns_list(self):
        """Verifica que retorna una lista"""
        response = client.get("/models")
        data = response.json()
        assert isinstance(data, list)
    
    def test_models_contains_5_models(self):
        """Verifica que hay 5 modelos disponibles"""
        response = client.get("/models")
        data = response.json()
        assert len(data) == 5
    
    def test_model_has_required_fields(self):
        """Verifica que cada modelo tiene los campos requeridos"""
        response = client.get("/models")
        data = response.json()
        for model in data:
            assert "name" in model
            assert "display_name" in model
            assert "trained" in model
            assert "accuracy" in model


class TestFeaturesEndpoint:
    """Tests para el endpoint /features"""
    
    def test_features_returns_200(self):
        """Verifica que el endpoint de features responde correctamente"""
        response = client.get("/features")
        assert response.status_code == 200
    
    def test_features_contains_30_features(self):
        """Verifica que hay 30 características"""
        response = client.get("/features")
        data = response.json()
        assert data["total_features"] == 30
    
    def test_features_has_categories(self):
        """Verifica que las categorías existen"""
        response = client.get("/features")
        data = response.json()
        assert "categories" in data
        assert "mean" in data["categories"]
        assert "error" in data["categories"]
        assert "worst" in data["categories"]


class TestTrainEndpoint:
    """Tests para el endpoint /train"""
    
    def test_train_random_forest(self):
        """Verifica que se puede entrenar Random Forest"""
        response = client.post("/train/random_forest")
        assert response.status_code == 200
        data = response.json()
        assert data["model"] == "random_forest"
        assert "accuracy" in data
        assert data["accuracy"] > 0
    
    def test_train_invalid_model(self):
        """Verifica que modelo inválido retorna 404"""
        response = client.post("/train/invalid_model")
        assert response.status_code == 404


class TestSampleDataEndpoint:
    """Tests para el endpoint /sample-data"""
    
    def test_sample_data_returns_200(self):
        """Verifica que el endpoint responde correctamente"""
        response = client.get("/sample-data")
        assert response.status_code == 200
    
    def test_sample_data_has_examples(self):
        """Verifica que contiene ejemplos maligno y benigno"""
        response = client.get("/sample-data")
        data = response.json()
        assert "malignant_example" in data
        assert "benign_example" in data
    
    def test_sample_data_has_30_features(self):
        """Verifica que los ejemplos tienen 30 características"""
        response = client.get("/sample-data")
        data = response.json()
        assert len(data["malignant_example"]) == 30
        assert len(data["benign_example"]) == 30


class TestRandomSampleEndpoint:
    """Tests para el endpoint /random-sample"""
    
    def test_random_sample_returns_200(self):
        """Verifica que el endpoint responde correctamente"""
        response = client.get("/random-sample")
        assert response.status_code == 200
    
    def test_random_sample_has_30_features(self):
        """Verifica que el sample aleatorio tiene 30 características"""
        response = client.get("/random-sample")
        data = response.json()
        assert "random_sample" in data
        assert len(data["random_sample"]) == 30


class TestPredictEndpoint:
    """Tests para el endpoint /predict"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Entrenar modelo antes de las pruebas de predicción"""
        client.post("/train/random_forest")
    
    def test_predict_malignant_case(self):
        """Verifica predicción de caso maligno"""
        # Obtener datos de ejemplo
        sample_response = client.get("/sample-data")
        malignant_data = sample_response.json()["malignant_example"]
        
        # Realizar predicción
        response = client.post("/predict", json={
            "model_name": "random_forest",
            "features": malignant_data
        })
        
        assert response.status_code == 200
        data = response.json()
        assert "prediction" in data
        assert data["prediction"] in ["Maligno", "Benigno"]
    
    def test_predict_returns_probabilities(self):
        """Verifica que la predicción incluye probabilidades"""
        sample_response = client.get("/sample-data")
        benign_data = sample_response.json()["benign_example"]
        
        response = client.post("/predict", json={
            "model_name": "random_forest",
            "features": benign_data
        })
        
        data = response.json()
        assert "probability_malignant" in data
        assert "probability_benign" in data
        assert 0 <= data["probability_malignant"] <= 100
        assert 0 <= data["probability_benign"] <= 100


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
