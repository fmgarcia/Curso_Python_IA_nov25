import React, { createContext, useContext, useState, useCallback, useEffect } from 'react';
import axios from 'axios';

// URL del API: usa variable de entorno en producción, localhost en desarrollo
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Crear contexto
const AppContext = createContext();

// Hook personalizado para usar el contexto
export const useAppContext = () => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useAppContext debe usarse dentro de AppProvider');
  }
  return context;
};

// Proveedor del contexto
export const AppProvider = ({ children }) => {
  // Estado de autenticación
  const [isAuthenticated, setIsAuthenticated] = useState(() => {
    return localStorage.getItem('isAuthenticated') === 'true';
  });
  const [user, setUser] = useState(() => {
    return localStorage.getItem('user') || null;
  });

  // Estado del tema (claro/oscuro)
  const [theme, setTheme] = useState(() => {
    const saved = localStorage.getItem('theme');
    return saved || 'light';
  });

  // Aplicar tema al documento
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  }, [theme]);

  // Función para cambiar tema
  const toggleTheme = useCallback(() => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  }, []);

  // Función de login
  const login = useCallback((username) => {
    setIsAuthenticated(true);
    setUser(username);
    localStorage.setItem('isAuthenticated', 'true');
    localStorage.setItem('user', username);
  }, []);

  // Función de logout
  const logout = useCallback(() => {
    setIsAuthenticated(false);
    setUser(null);
    localStorage.removeItem('isAuthenticated');
    localStorage.removeItem('user');
  }, []);

  const [models, setModels] = useState([]);
  const [selectedModel, setSelectedModel] = useState('');
  const [features, setFeatures] = useState({});
  const [featureNames, setFeatureNames] = useState([]);
  const [featureCategories, setFeatureCategories] = useState({});
  const [predictionResult, setPredictionResult] = useState(null);
  const [loading, setLoading] = useState({
    models: false,
    training: false,
    predicting: false,
    features: false
  });
  const [error, setError] = useState(null);
  const [successMessage, setSuccessMessage] = useState(null);
  
  // Estado del dataset
  const [datasetInfo, setDatasetInfo] = useState({
    name: "Wisconsin Breast Cancer (Original)",
    samples: 569,
    is_custom: false
  });

  // Obtener información del dataset actual
  const fetchDatasetInfo = useCallback(async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/dataset-info`);
      setDatasetInfo(response.data);
    } catch (err) {
      console.error('Error al obtener info del dataset:', err);
    }
  }, []);

  // Subir dataset personalizado
  const uploadDataset = useCallback(async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    
    try {
      const response = await axios.post(`${API_BASE_URL}/upload-dataset`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      setDatasetInfo(response.data.dataset_info);
      setSuccessMessage(response.data.message);
      return response.data;
    } catch (err) {
      const errorMsg = err.response?.data?.detail || 'Error al subir el dataset';
      setError(errorMsg);
      throw new Error(errorMsg);
    }
  }, []);

  // Resetear al dataset original
  const resetDataset = useCallback(async () => {
    try {
      const response = await axios.post(`${API_BASE_URL}/reset-dataset`);
      setDatasetInfo(response.data.dataset_info);
      setSuccessMessage(response.data.message);
    } catch (err) {
      setError('Error al resetear el dataset');
    }
  }, []);

  // Generar datos sintéticos
  const generateSyntheticData = useCallback(async (numSamples) => {
    try {
      const response = await axios.post(
        `${API_BASE_URL}/generate-synthetic-data`,
        { num_samples: numSamples },
        { responseType: 'blob' }
      );
      
      // Crear URL para descarga
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `synthetic_tumor_data_${numSamples}_samples.csv`);
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);
      
      setSuccessMessage(`Dataset sintético de ${numSamples} muestras generado y descargado`);
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al generar datos sintéticos');
    }
  }, []);

  // Obtener lista de modelos
  const fetchModels = useCallback(async () => {
    setLoading(prev => ({ ...prev, models: true }));
    setError(null);
    try {
      const response = await axios.get(`${API_BASE_URL}/models`);
      setModels(response.data);
      if (!selectedModel && response.data.length > 0) {
        setSelectedModel(response.data[0].name);
      }
    } catch (err) {
      setError('Error al obtener la lista de modelos. Asegúrate de que el backend esté ejecutándose.');
      console.error(err);
    } finally {
      setLoading(prev => ({ ...prev, models: false }));
    }
  }, [selectedModel]);

  // Obtener características requeridas
  const fetchFeatures = useCallback(async () => {
    setLoading(prev => ({ ...prev, features: true }));
    try {
      const response = await axios.get(`${API_BASE_URL}/features`);
      setFeatureNames(response.data.feature_names);
      setFeatureCategories(response.data.categories);
      
      // Inicializar formulario con valores vacíos
      const initialFeatures = {};
      response.data.feature_names.forEach(name => {
        initialFeatures[name] = '';
      });
      setFeatures(initialFeatures);
    } catch (err) {
      console.error('Error al obtener características:', err);
    } finally {
      setLoading(prev => ({ ...prev, features: false }));
    }
  }, []);

  // Entrenar modelo
  const trainModel = useCallback(async (modelName) => {
    setLoading(prev => ({ ...prev, training: true }));
    setError(null);
    setSuccessMessage(null);
    try {
      const response = await axios.post(`${API_BASE_URL}/train/${modelName}`);
      setSuccessMessage(`${response.data.message} - Accuracy: ${response.data.accuracy}%`);
      // Actualizar lista de modelos
      await fetchModels();
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al entrenar el modelo');
      console.error(err);
    } finally {
      setLoading(prev => ({ ...prev, training: false }));
    }
  }, [fetchModels]);

  // Realizar predicción
  const predict = useCallback(async () => {
    if (!selectedModel) {
      setError('Por favor, selecciona un modelo');
      return;
    }

    // Validar que todos los campos tengan valores
    const emptyFields = Object.entries(features).filter(([_, value]) => value === '' || value === null);
    if (emptyFields.length > 0) {
      setError(`Por favor, completa todos los campos del formulario`);
      return;
    }

    setLoading(prev => ({ ...prev, predicting: true }));
    setError(null);
    setPredictionResult(null);

    try {
      // Convertir valores a números
      const numericFeatures = {};
      for (const [key, value] of Object.entries(features)) {
        numericFeatures[key] = parseFloat(value);
      }

      const response = await axios.post(`${API_BASE_URL}/predict`, {
        model_name: selectedModel,
        features: numericFeatures
      });
      
      setPredictionResult(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al realizar la predicción');
      console.error(err);
    } finally {
      setLoading(prev => ({ ...prev, predicting: false }));
    }
  }, [selectedModel, features]);

  // Cargar datos de ejemplo
  const loadSampleData = useCallback(async (type) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/sample-data`);
      const sampleData = type === 'malignant' 
        ? response.data.malignant_example 
        : response.data.benign_example;
      setFeatures(sampleData);
      setPredictionResult(null);
    } catch (err) {
      setError('Error al cargar datos de ejemplo');
      console.error(err);
    }
  }, []);

  // Cargar datos aleatorios realistas
  const loadRandomData = useCallback(async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/random-sample`);
      setFeatures(response.data.random_sample);
      setPredictionResult(null);
    } catch (err) {
      setError('Error al generar datos aleatorios');
      console.error(err);
    }
  }, []);

  // Actualizar un campo del formulario
  const updateFeature = useCallback((name, value) => {
    setFeatures(prev => ({ ...prev, [name]: value }));
  }, []);

  // Limpiar formulario
  const clearForm = useCallback(() => {
    const clearedFeatures = {};
    featureNames.forEach(name => {
      clearedFeatures[name] = '';
    });
    setFeatures(clearedFeatures);
    setPredictionResult(null);
    setError(null);
    setSuccessMessage(null);
  }, [featureNames]);

  // Limpiar mensajes
  const clearMessages = useCallback(() => {
    setError(null);
    setSuccessMessage(null);
  }, []);

  const value = {
    // Autenticación
    isAuthenticated,
    user,
    login,
    logout,
    // Tema
    theme,
    toggleTheme,
    // Dataset
    datasetInfo,
    fetchDatasetInfo,
    uploadDataset,
    resetDataset,
    generateSyntheticData,
    // Modelos y predicción
    models,
    selectedModel,
    setSelectedModel,
    features,
    featureNames,
    featureCategories,
    predictionResult,
    loading,
    error,
    successMessage,
    fetchModels,
    fetchFeatures,
    trainModel,
    predict,
    loadSampleData,
    loadRandomData,
    updateFeature,
    clearForm,
    clearMessages
  };

  return (
    <AppContext.Provider value={value}>
      {children}
    </AppContext.Provider>
  );
};

export default AppContext;
