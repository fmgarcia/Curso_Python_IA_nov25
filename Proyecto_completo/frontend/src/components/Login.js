import React, { useState } from 'react';
import { useAppContext } from '../context/AppContext';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  
  const { login, theme, toggleTheme } = useAppContext();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    // Simular un pequeño delay para mejor UX
    await new Promise(resolve => setTimeout(resolve, 500));

    // Credenciales hardcodeadas: admin/admin
    if (username === 'admin' && password === 'admin') {
      login(username);
    } else {
      setError('❌ Credenciales incorrectas. Por favor, inténtalo de nuevo.');
    }
    
    setLoading(false);
  };

  return (
    <div className="login-container">
      {/* Botón de cambio de tema */}
      <button 
        className="theme-toggle login-theme-toggle"
        onClick={toggleTheme}
        aria-label={theme === 'light' ? 'Activar modo oscuro' : 'Activar modo claro'}
        title={theme === 'light' ? 'Modo oscuro' : 'Modo claro'}
      >
        {theme === 'light' ? '🌙' : '☀️'}
      </button>

      <div className="login-card">
        <div className="login-header">
          <div className="login-logo">🔬</div>
          <h1 className="login-title">Sistema de Detección</h1>
          <p className="login-subtitle">Detección de Tumores con Machine Learning</p>
        </div>

        <form className="login-form" onSubmit={handleSubmit}>
          <div className="login-input-group">
            <label htmlFor="username">Usuario</label>
            <input
              type="text"
              id="username"
              className="login-input"
              placeholder="Introduce tu usuario"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
              autoComplete="username"
              disabled={loading}
            />
          </div>

          <div className="login-input-group">
            <label htmlFor="password">Contraseña</label>
            <input
              type="password"
              id="password"
              className="login-input"
              placeholder="Introduce tu contraseña"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              autoComplete="current-password"
              disabled={loading}
            />
          </div>

          {error && (
            <div className="login-error">
              {error}
            </div>
          )}

          <button 
            type="submit" 
            className="btn btn-primary login-btn"
            disabled={loading}
          >
            {loading ? (
              <>
                <span className="spinner"></span>
                Iniciando sesión...
              </>
            ) : (
              <>
                🔐 Iniciar Sesión
              </>
            )}
          </button>
        </form>

        {/* Mostrar credenciales de prueba */}
        <div className="login-help">
          <p>🔑 Credenciales de acceso:</p>
          <div className="login-credentials">
            <span>👤 admin</span>
            <span>🔒 admin</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
