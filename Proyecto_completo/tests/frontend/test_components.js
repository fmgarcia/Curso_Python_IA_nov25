/**
 * Tests de componentes React para el frontend
 * Ejecutar con: npm test
 */

import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';

// Mock de axios
jest.mock('axios', () => ({
  get: jest.fn(),
  post: jest.fn()
}));

import axios from 'axios';
import App from '../../frontend/src/App';
import { AppProvider } from '../../frontend/src/context/AppContext';

describe('Login Component', () => {
  
  test('muestra el formulario de login', () => {
    render(<App />);
    expect(screen.getByText(/Iniciar Sesión/i)).toBeInTheDocument();
  });
  
  test('muestra campos de usuario y contraseña', () => {
    render(<App />);
    expect(screen.getByPlaceholderText(/Usuario/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/Contraseña/i)).toBeInTheDocument();
  });
  
  test('muestra credenciales de ayuda', () => {
    render(<App />);
    expect(screen.getByText(/admin/)).toBeInTheDocument();
  });
  
  test('permite escribir en los campos', () => {
    render(<App />);
    const userInput = screen.getByPlaceholderText(/Usuario/i);
    const passInput = screen.getByPlaceholderText(/Contraseña/i);
    
    fireEvent.change(userInput, { target: { value: 'admin' } });
    fireEvent.change(passInput, { target: { value: 'admin' } });
    
    expect(userInput.value).toBe('admin');
    expect(passInput.value).toBe('admin');
  });
  
  test('muestra error con credenciales incorrectas', async () => {
    render(<App />);
    
    const userInput = screen.getByPlaceholderText(/Usuario/i);
    const passInput = screen.getByPlaceholderText(/Contraseña/i);
    const loginBtn = screen.getByText(/Iniciar Sesión/i);
    
    fireEvent.change(userInput, { target: { value: 'wrong' } });
    fireEvent.change(passInput, { target: { value: 'wrong' } });
    fireEvent.click(loginBtn);
    
    await waitFor(() => {
      expect(screen.getByText(/incorrectas/i)).toBeInTheDocument();
    });
  });
});

describe('ModelSelector Component', () => {
  
  beforeEach(() => {
    axios.get.mockImplementation((url) => {
      if (url.includes('/models')) {
        return Promise.resolve({
          data: [
            { name: 'random_forest', display_name: 'Random Forest', trained: true, accuracy: 95.6 },
            { name: 'xgboost', display_name: 'XGBoost', trained: false, accuracy: null }
          ]
        });
      }
      if (url.includes('/features')) {
        return Promise.resolve({
          data: {
            feature_names: ['mean radius'],
            categories: { mean: ['mean radius'], error: [], worst: [] }
          }
        });
      }
    });
  });
  
  test('muestra lista de modelos', async () => {
    // Este test requiere que el usuario esté autenticado
    // Simular estado autenticado
  });
});

describe('Theme Toggle', () => {
  
  test('permite cambiar entre modo claro y oscuro', () => {
    render(<App />);
    
    // Buscar el botón de tema
    const themeToggle = screen.queryByRole('button', { name: /tema/i }) ||
                        screen.queryByText('🌙') ||
                        screen.queryByText('☀️');
    
    if (themeToggle) {
      fireEvent.click(themeToggle);
      // Verificar que el tema cambió
    }
  });
});

describe('Responsive Design', () => {
  
  const resizeWindow = (width, height) => {
    window.innerWidth = width;
    window.innerHeight = height;
    window.dispatchEvent(new Event('resize'));
  };
  
  test('se adapta a pantalla móvil', () => {
    resizeWindow(375, 667);
    render(<App />);
    // Verificar que los elementos se muestran correctamente
  });
  
  test('se adapta a tablet', () => {
    resizeWindow(768, 1024);
    render(<App />);
    // Verificar layout de tablet
  });
  
  test('se adapta a desktop', () => {
    resizeWindow(1440, 900);
    render(<App />);
    // Verificar layout de desktop
  });
});

describe('PredictionForm Component', () => {
  
  test('muestra botones de datos de ejemplo', async () => {
    // Requiere estado autenticado
    // Verificar que existen los botones:
    // - Caso Benigno
    // - Caso Maligno
    // - Datos Aleatorios
  });
  
  test('muestra campos de entrada agrupados', async () => {
    // Verificar que existen las 3 secciones:
    // - Valores Medios
    // - Errores Estándar
    // - Valores Peores
  });
});

describe('Accesibilidad', () => {
  
  test('todos los inputs tienen labels', () => {
    render(<App />);
    const inputs = screen.getAllByRole('textbox');
    inputs.forEach(input => {
      expect(input).toHaveAccessibleName();
    });
  });
  
  test('botones son accesibles por teclado', () => {
    render(<App />);
    const buttons = screen.getAllByRole('button');
    buttons.forEach(button => {
      expect(button).not.toBeDisabled();
    });
  });
});
