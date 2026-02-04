import React from 'react';
import { useAppContext } from '../context/AppContext';

const PredictionForm = () => {
  const {
    features,
    featureCategories,
    updateFeature,
    predict,
    loadSampleData,
    loadRandomData,
    clearForm,
    loading,
    models,
    selectedModel
  } = useAppContext();

  const handleSubmit = (e) => {
    e.preventDefault();
    predict();
  };

  const selectedModelData = models.find(m => m.name === selectedModel);
  const isModelTrained = selectedModelData?.trained;

  // Etiquetas amigables para las características
  const featureLabels = {
    'mean radius': 'Radio medio',
    'mean texture': 'Textura media',
    'mean perimeter': 'Perímetro medio',
    'mean area': 'Área media',
    'mean smoothness': 'Suavidad media',
    'mean compactness': 'Compacidad media',
    'mean concavity': 'Concavidad media',
    'mean concave points': 'Puntos cóncavos medios',
    'mean symmetry': 'Simetría media',
    'mean fractal dimension': 'Dimensión fractal media',
    'radius error': 'Error de radio',
    'texture error': 'Error de textura',
    'perimeter error': 'Error de perímetro',
    'area error': 'Error de área',
    'smoothness error': 'Error de suavidad',
    'compactness error': 'Error de compacidad',
    'concavity error': 'Error de concavidad',
    'concave points error': 'Error de puntos cóncavos',
    'symmetry error': 'Error de simetría',
    'fractal dimension error': 'Error de dim. fractal',
    'worst radius': 'Peor radio',
    'worst texture': 'Peor textura',
    'worst perimeter': 'Peor perímetro',
    'worst area': 'Peor área',
    'worst smoothness': 'Peor suavidad',
    'worst compactness': 'Peor compacidad',
    'worst concavity': 'Peor concavidad',
    'worst concave points': 'Peor puntos cóncavos',
    'worst symmetry': 'Peor simetría',
    'worst fractal dimension': 'Peor dim. fractal'
  };

  const renderFeatureGroup = (category, title, icon) => {
    const categoryFeatures = featureCategories[category] || [];
    
    return (
      <div className="form-section">
        <h3 className="form-section-title">
          <span>{icon}</span>
          {title}
        </h3>
        <div className="form-grid">
          {categoryFeatures.map(name => (
            <div key={name} className="form-group">
              <label className="form-label" title={name}>
                {featureLabels[name] || name}
              </label>
              <input
                type="number"
                step="any"
                className="form-input"
                value={features[name] || ''}
                onChange={(e) => updateFeature(name, e.target.value)}
                placeholder={name}
              />
            </div>
          ))}
        </div>
      </div>
    );
  };

  return (
    <div className="card">
      <div className="card-header">
        <h2 className="card-title">📋 Datos del Tumor</h2>
      </div>

      {!isModelTrained && (
        <div className="alert alert-info">
          <span>ℹ️</span>
          <span>El modelo seleccionado no está entrenado. Por favor, entrénalo primero.</span>
        </div>
      )}

      <form onSubmit={handleSubmit}>
        {/* Datos de ejemplo y acciones - ARRIBA */}
        <div className="sample-data-section" style={{ marginBottom: '1.5rem' }}>
          <p style={{ fontSize: '0.9rem', color: 'var(--text-muted)', marginBottom: '0.75rem' }}>
            💡 Cargar datos de ejemplo para probar:
          </p>
          <div className="sample-buttons">
            <button
              type="button"
              className="btn btn-secondary btn-sample"
              onClick={() => loadSampleData('benign')}
            >
              🟢 Caso Benigno
            </button>
            <button
              type="button"
              className="btn btn-secondary btn-sample"
              onClick={() => loadSampleData('malignant')}
            >
              🔴 Caso Maligno
            </button>
            <button
              type="button"
              className="btn btn-secondary btn-sample"
              onClick={loadRandomData}
              style={{ background: '#805ad5', color: 'white' }}
            >
              🎲 Datos Aleatorios
            </button>
          </div>
        </div>

        {/* Acciones principales */}
        <div className="form-actions" style={{ marginBottom: '1.5rem' }}>
          <button
            type="submit"
            className="btn btn-success"
            disabled={loading.predicting || !isModelTrained}
            style={{ flex: 2 }}
          >
            {loading.predicting ? (
              <>
                <span className="spinner"></span>
                Analizando...
              </>
            ) : (
              <>
                🔬 Realizar Predicción
              </>
            )}
          </button>
          <button
            type="button"
            className="btn btn-secondary"
            onClick={clearForm}
            style={{ flex: 1 }}
          >
            🗑️ Limpiar
          </button>
        </div>

        {/* Sección Mean */}
        {renderFeatureGroup('mean', 'Valores Medios', '📊')}
        
        {/* Sección Error */}
        {renderFeatureGroup('error', 'Errores Estándar', '📈')}
        
        {/* Sección Worst */}
        {renderFeatureGroup('worst', 'Valores Peores (Máximos)', '⚠️')}
      </form>
    </div>
  );
};

export default PredictionForm;
