import React from 'react';
import { useAppContext } from '../context/AppContext';

const PredictionResult = () => {
  const { predictionResult, selectedModel, models } = useAppContext();

  if (!predictionResult) {
    return null;
  }

  const isBenign = predictionResult.prediction === 'Benigno';
  const selectedModelData = models.find(m => m.name === selectedModel);

  return (
    <div className="card">
      <div className="card-header">
        <h2 className="card-title">🔬 Resultado del Análisis</h2>
        <span style={{ fontSize: '0.85rem', color: '#718096' }}>
          Modelo: {selectedModelData?.display_name}
        </span>
      </div>

      <div className={`result-card ${isBenign ? 'result-benign' : 'result-malignant'}`}>
        <div className="result-icon">
          {isBenign ? '✅' : '⚠️'}
        </div>
        
        <h3 className="result-title">
          {predictionResult.prediction}
        </h3>
        
        <p className="result-subtitle">
          {isBenign 
            ? 'El tumor analizado presenta características benignas'
            : 'El tumor analizado presenta características malignas - Se recomienda consulta médica inmediata'
          }
        </p>

        <div className="probability-bars">
          <div className="probability-item">
            <span className="probability-label">Benigno</span>
            <div className="probability-bar">
              <div 
                className="probability-fill benign"
                style={{ width: `${predictionResult.probability_benign}%` }}
              />
            </div>
            <span className="probability-value">{predictionResult.probability_benign}%</span>
          </div>
          
          <div className="probability-item">
            <span className="probability-label">Maligno</span>
            <div className="probability-bar">
              <div 
                className="probability-fill malignant"
                style={{ width: `${predictionResult.probability_malignant}%` }}
              />
            </div>
            <span className="probability-value">{predictionResult.probability_malignant}%</span>
          </div>
        </div>

        <p style={{ 
          marginTop: '1.5rem', 
          fontSize: '0.85rem', 
          opacity: 0.8,
          fontStyle: 'italic'
        }}>
          ⚕️ Este resultado es orientativo y no sustituye el diagnóstico médico profesional
        </p>
      </div>
    </div>
  );
};

export default PredictionResult;
