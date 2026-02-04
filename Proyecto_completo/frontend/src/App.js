import React, { useEffect } from 'react';
import { AppProvider, useAppContext } from './context/AppContext';
import ModelSelector from './components/ModelSelector';
import PredictionForm from './components/PredictionForm';
import PredictionResult from './components/PredictionResult';
import Login from './components/Login';
import './index.css';

const Dashboard = () => {
  const { 
    fetchModels, 
    fetchFeatures, 
    loading, 
    isAuthenticated, 
    user, 
    logout, 
    theme, 
    toggleTheme 
  } = useAppContext();

  useEffect(() => {
    if (isAuthenticated) {
      fetchModels();
      fetchFeatures();
    }
  }, [fetchModels, fetchFeatures, isAuthenticated]);

  // Si no está autenticado, mostrar login
  if (!isAuthenticated) {
    return <Login />;
  }

  if (loading.models && loading.features) {
    return (
      <div className="app-container">
        <div className="header">
          <h1>🏥 Centro Médico - Detección de Tumores</h1>
          <p>Cargando sistema de inteligencia artificial...</p>
        </div>
        <div className="card" style={{ textAlign: 'center', padding: '3rem' }}>
          <div className="spinner" style={{ margin: '0 auto', width: '40px', height: '40px' }}></div>
          <p style={{ marginTop: '1rem', color: '#718096' }}>Conectando con el servidor...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="app-container">
      {/* Header */}
      <header className="header">
        <div className="header-controls">
          <button 
            className="theme-toggle"
            onClick={toggleTheme}
            aria-label={theme === 'light' ? 'Activar modo oscuro' : 'Activar modo claro'}
            title={theme === 'light' ? 'Modo oscuro' : 'Modo claro'}
          >
            {theme === 'light' ? '🌙' : '☀️'}
          </button>
          <button 
            className="logout-btn"
            onClick={logout}
            title="Cerrar sesión"
          >
            👤 {user} | Salir
          </button>
        </div>
        <div className="header-content">
          <h1>🏥 Centro Médico - Detección de Tumores</h1>
          <p>Sistema de Inteligencia Artificial para diagnóstico de tumores mamarios</p>
        </div>
      </header>

      {/* Contenido principal */}
      <main className="main-grid">
        {/* Panel lateral */}
        <aside>
          <ModelSelector />
        </aside>

        {/* Área principal */}
        <section>
          <PredictionResult />
          <PredictionForm />
        </section>
      </main>

      {/* Footer */}
      <footer style={{ 
        textAlign: 'center', 
        marginTop: '2rem', 
        color: 'rgba(255,255,255,0.7)',
        fontSize: '0.85rem'
      }}>
        <p>
          Sistema desarrollado con fines educativos | 
          Dataset: Wisconsin Breast Cancer | 
          Los resultados no sustituyen el diagnóstico médico profesional
        </p>
      </footer>
    </div>
  );
};

function App() {
  return (
    <AppProvider>
      <Dashboard />
    </AppProvider>
  );
}

export default App;
