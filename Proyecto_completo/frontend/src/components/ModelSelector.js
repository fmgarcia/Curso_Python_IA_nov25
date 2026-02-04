import React, { useState, useEffect, useRef } from 'react';
import { useAppContext } from '../context/AppContext';

const ModelSelector = () => {
  const {
    models,
    selectedModel,
    setSelectedModel,
    trainModel,
    loading,
    successMessage,
    error,
    clearMessages,
    datasetInfo,
    fetchDatasetInfo,
    uploadDataset,
    resetDataset,
    generateSyntheticData
  } = useAppContext();

  const [numSamples, setNumSamples] = useState(100);
  const [uploadedFileName, setUploadedFileName] = useState('');
  const [isGenerating, setIsGenerating] = useState(false);
  const fileInputRef = useRef(null);

  useEffect(() => {
    fetchDatasetInfo();
  }, [fetchDatasetInfo]);

  const handleTrain = () => {
    if (selectedModel) {
      trainModel(selectedModel);
    }
  };

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (file) {
      setUploadedFileName(file.name);
      try {
        await uploadDataset(file);
      } catch (err) {
        setUploadedFileName('');
      }
    }
  };

  const handleResetDataset = async () => {
    await resetDataset();
    setUploadedFileName('');
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const handleGenerateSynthetic = async () => {
    if (numSamples < 1 || numSamples > 10000) {
      return;
    }
    setIsGenerating(true);
    try {
      await generateSyntheticData(numSamples);
    } finally {
      setIsGenerating(false);
    }
  };

  const selectedModelData = models.find(m => m.name === selectedModel);

  return (
    <div className="card">
      <div className="card-header">
        <h2 className="card-title">🤖 Panel de Control</h2>
      </div>

      {/* Mensajes de éxito/error */}
      {successMessage && (
        <div className="alert alert-success">
          <span>✅</span>
          <span>{successMessage}</span>
          <button 
            onClick={clearMessages}
            style={{ marginLeft: 'auto', background: 'none', border: 'none', cursor: 'pointer', color: 'inherit' }}
          >
            ✕
          </button>
        </div>
      )}

      {error && (
        <div className="alert alert-error">
          <span>❌</span>
          <span>{error}</span>
          <button 
            onClick={clearMessages}
            style={{ marginLeft: 'auto', background: 'none', border: 'none', cursor: 'pointer', color: 'inherit' }}
          >
            ✕
          </button>
        </div>
      )}

      {/* Sección de Dataset */}
      <div className="dataset-section">
        <h3 className="dataset-section-title">📊 Dataset de Entrenamiento</h3>
        
        {/* Info del dataset actual */}
        <div className={`dataset-info ${datasetInfo.is_custom ? 'custom' : ''}`}>
          <span>{datasetInfo.is_custom ? '📁' : '🔬'}</span>
          <span>
            <strong>{datasetInfo.name}</strong>
            <br />
            <small>{datasetInfo.samples} muestras</small>
            {datasetInfo.is_custom && datasetInfo.malignant_count !== undefined && (
              <small> • {datasetInfo.malignant_count} malignas, {datasetInfo.benign_count} benignas</small>
            )}
          </span>
        </div>

        {/* Subir dataset personalizado */}
        <div className="file-input-wrapper">
          <input
            type="file"
            accept=".csv"
            onChange={handleFileChange}
            className="file-input"
            id="dataset-file"
            ref={fileInputRef}
          />
          <label htmlFor="dataset-file" className="file-input-label">
            📤 {uploadedFileName || 'Subir CSV personalizado'}
          </label>
        </div>

        {/* Botón de resetear */}
        {datasetInfo.is_custom && (
          <div className="dataset-actions">
            <button 
              className="btn btn-secondary btn-small"
              onClick={handleResetDataset}
            >
              🔄 Usar dataset original
            </button>
          </div>
        )}
      </div>

      {/* Sección de generación de datos sintéticos */}
      <div className="synthetic-section">
        <h3 className="dataset-section-title">🧪 Generar Datos Sintéticos</h3>
        <div className="synthetic-form">
          <div className="synthetic-input-group">
            <label htmlFor="num-samples">Nº de muestras</label>
            <input
              type="number"
              id="num-samples"
              className="synthetic-input"
              value={numSamples}
              onChange={(e) => setNumSamples(parseInt(e.target.value) || 0)}
              min="1"
              max="10000"
              placeholder="100"
            />
          </div>
          <button
            className="btn btn-generate"
            onClick={handleGenerateSynthetic}
            disabled={isGenerating || numSamples < 1 || numSamples > 10000}
          >
            {isGenerating ? (
              <>
                <span className="spinner"></span>
                Generando...
              </>
            ) : (
              <>
                ⬇️ Descargar CSV
              </>
            )}
          </button>
        </div>
        <small style={{ color: 'var(--text-muted)', marginTop: '0.5rem', display: 'block' }}>
          Genera datos sintéticos realistas para entrenar el modelo (máx. 10.000)
        </small>
      </div>

      {/* Selector de modelo */}
      <div style={{ marginTop: '1.5rem', marginBottom: '1rem' }}>
        <label className="form-label" style={{ marginBottom: '0.5rem', display: 'block' }}>
          Seleccionar Modelo de IA
        </label>
        <select
          className="model-selector"
          value={selectedModel}
          onChange={(e) => setSelectedModel(e.target.value)}
          disabled={loading.models}
        >
          {models.map(model => (
            <option key={model.name} value={model.name}>
              {model.display_name} {model.trained ? '✓' : '○'}
            </option>
          ))}
        </select>
      </div>

      {/* Botón de entrenamiento */}
      <button
        className="btn btn-primary btn-block"
        onClick={handleTrain}
        disabled={loading.training || !selectedModel}
      >
        {loading.training ? (
          <>
            <span className="spinner"></span>
            Entrenando...
          </>
        ) : (
          <>
            🎯 Entrenar {selectedModelData?.display_name || 'Modelo'}
          </>
        )}
      </button>

      {/* Lista de modelos */}
      <div className="models-list">
        <h3 className="models-list-title">
          Estado de los Modelos
        </h3>
        {models.map(model => (
          <div 
            key={model.name} 
            className={`model-item ${model.name === selectedModel ? 'model-item-selected' : ''}`}
          >
            <span className="model-name">{model.display_name}</span>
            <div className="model-item-badges">
              {model.trained && model.accuracy && (
                <span className="accuracy-badge">
                  {model.accuracy}%
                </span>
              )}
              <span className={`status-badge ${model.trained ? 'status-trained' : 'status-not-trained'}`}>
                {model.trained ? 'Entrenado' : 'Sin entrenar'}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ModelSelector;
