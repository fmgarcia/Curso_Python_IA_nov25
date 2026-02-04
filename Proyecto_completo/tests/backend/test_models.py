# pyright: reportMissingImports=false
"""
Tests de modelos ML para el backend de detección de tumores
"""
import pytest
import os
import sys

# Añadir path del backend
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'backend'))

from models import random_forest, xgboost_model, adaboost, gradient_boosting, voting_model  # type: ignore


class TestRandomForestModel:
    """Tests para el modelo Random Forest"""
    
    def test_train_returns_dict(self):
        """Verifica que train() retorna un diccionario"""
        result = random_forest.train()
        assert isinstance(result, dict)
    
    def test_train_has_accuracy(self):
        """Verifica que el resultado incluye accuracy"""
        result = random_forest.train()
        assert "accuracy" in result
        assert result["accuracy"] > 0
        assert result["accuracy"] <= 100
    
    def test_is_trained_after_training(self):
        """Verifica que is_trained() retorna True después de entrenar"""
        random_forest.train()
        assert random_forest.is_trained() == True
    
    def test_get_accuracy_returns_value(self):
        """Verifica que get_accuracy() retorna un valor"""
        random_forest.train()
        accuracy = random_forest.get_accuracy()
        assert accuracy is not None
        assert accuracy > 0


class TestXGBoostModel:
    """Tests para el modelo XGBoost"""
    
    def test_train_returns_dict(self):
        """Verifica que train() retorna un diccionario"""
        result = xgboost_model.train()
        assert isinstance(result, dict)
    
    def test_train_has_model_name(self):
        """Verifica que el resultado incluye el nombre del modelo"""
        result = xgboost_model.train()
        assert result["model"] == "xgboost"
    
    def test_accuracy_is_reasonable(self):
        """Verifica que el accuracy está en un rango razonable"""
        result = xgboost_model.train()
        # El accuracy debería ser al menos 80% para este dataset
        assert result["accuracy"] >= 80


class TestAdaBoostModel:
    """Tests para el modelo AdaBoost"""
    
    def test_train_success(self):
        """Verifica que el entrenamiento es exitoso"""
        result = adaboost.train()
        assert "message" in result
        assert "entrenado" in result["message"].lower()
    
    def test_predict_after_training(self):
        """Verifica que se puede predecir después de entrenar"""
        adaboost.train()
        
        # Crear features de ejemplo
        features = {
            "mean radius": 14.0, "mean texture": 20.0, "mean perimeter": 90.0,
            "mean area": 600.0, "mean smoothness": 0.1, "mean compactness": 0.15,
            "mean concavity": 0.1, "mean concave points": 0.05, "mean symmetry": 0.2,
            "mean fractal dimension": 0.06, "radius error": 0.3, "texture error": 1.0,
            "perimeter error": 2.0, "area error": 30.0, "smoothness error": 0.005,
            "compactness error": 0.02, "concavity error": 0.03, "concave points error": 0.01,
            "symmetry error": 0.02, "fractal dimension error": 0.003, "worst radius": 16.0,
            "worst texture": 25.0, "worst perimeter": 110.0, "worst area": 800.0,
            "worst smoothness": 0.15, "worst compactness": 0.3, "worst concavity": 0.3,
            "worst concave points": 0.1, "worst symmetry": 0.3, "worst fractal dimension": 0.08
        }
        
        result = adaboost.predict(features)
        assert "prediction" in result
        assert result["prediction"] in ["Maligno", "Benigno"]


class TestGradientBoostingModel:
    """Tests para el modelo Gradient Boosting"""
    
    def test_train_and_predict(self):
        """Test completo de entrenamiento y predicción"""
        # Entrenar
        train_result = gradient_boosting.train()
        assert train_result["accuracy"] > 0
        
        # Predecir
        features = {
            "mean radius": 17.99, "mean texture": 10.38, "mean perimeter": 122.8,
            "mean area": 1001.0, "mean smoothness": 0.1184, "mean compactness": 0.2776,
            "mean concavity": 0.3001, "mean concave points": 0.1471, "mean symmetry": 0.2419,
            "mean fractal dimension": 0.07871, "radius error": 1.095, "texture error": 0.9053,
            "perimeter error": 8.589, "area error": 153.4, "smoothness error": 0.006399,
            "compactness error": 0.04904, "concavity error": 0.05373, "concave points error": 0.01587,
            "symmetry error": 0.03003, "fractal dimension error": 0.006193, "worst radius": 25.38,
            "worst texture": 17.33, "worst perimeter": 184.6, "worst area": 2019.0,
            "worst smoothness": 0.1622, "worst compactness": 0.6656, "worst concavity": 0.7119,
            "worst concave points": 0.2654, "worst symmetry": 0.4601, "worst fractal dimension": 0.1189
        }
        
        predict_result = gradient_boosting.predict(features)
        assert "probability_malignant" in predict_result
        assert "probability_benign" in predict_result


class TestVotingModel:
    """Tests para el modelo Voting Classifier"""
    
    def test_train_returns_correct_model_name(self):
        """Verifica que retorna el nombre correcto"""
        result = voting_model.train()
        assert result["model"] == "voting"
    
    def test_voting_combines_models(self):
        """Verifica que el Voting Classifier funciona"""
        voting_model.train()
        assert voting_model.is_trained() == True


class TestModelPersistence:
    """Tests para la persistencia de modelos"""
    
    def test_weights_directory_exists(self):
        """Verifica que el directorio de pesos existe después de entrenar"""
        random_forest.train()
        weights_path = os.path.join(
            os.path.dirname(__file__), 
            '..', '..', 'backend', 'weights'
        )
        assert os.path.exists(weights_path)
    
    def test_model_file_exists(self):
        """Verifica que el archivo del modelo existe"""
        random_forest.train()
        model_path = os.path.join(
            os.path.dirname(__file__), 
            '..', '..', 'backend', 'weights', 'random_forest.joblib'
        )
        assert os.path.exists(model_path)
    
    def test_accuracy_file_exists(self):
        """Verifica que el archivo de accuracy existe"""
        random_forest.train()
        accuracy_path = os.path.join(
            os.path.dirname(__file__), 
            '..', '..', 'backend', 'weights', 'random_forest_accuracy.json'
        )
        assert os.path.exists(accuracy_path)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
