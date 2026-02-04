# 🧪 Guía de Testing

## Visión General

El proyecto incluye pruebas para asegurar la calidad del código, la funcionalidad correcta y una buena experiencia de usuario.

---

## 📁 Estructura de Tests

```
tests/
├── backend/
│   ├── test_api.py           # Tests de endpoints API
│   ├── test_models.py        # Tests de modelos ML
│   └── test_integration.py   # Tests de integración
│
└── frontend/
    ├── test_components.js    # Tests de componentes React
    ├── test_usability.js     # Tests de usabilidad
    └── test_responsive.js    # Tests de responsividad
```

---

## 🔧 Backend Testing

### Ejecutar Tests
```powershell
cd backend
.\venv\Scripts\Activate.ps1
pip install pytest pytest-asyncio httpx
pytest tests/ -v
```

### Tests de API
- Verificar endpoints responden correctamente
- Validar esquemas de respuesta
- Probar casos de error

### Tests de Modelos
- Verificar entrenamiento exitoso
- Validar predicciones
- Comprobar persistencia de pesos

---

## 🎨 Frontend Testing

### Ejecutar Tests
```powershell
cd frontend
npm test
```

### Tests de Componentes
- Renderizado correcto
- Manejo de estado
- Interacciones de usuario

### Tests de Usabilidad
- Flujo de login
- Entrenamiento de modelos
- Proceso de predicción

### Tests de Responsividad
- Móvil (320px - 480px)
- Tablet (768px - 1024px)
- Desktop (1024px+)

---

## 📋 Checklist de Testing Manual

### Funcionalidad

- [ ] Login con credenciales correctas
- [ ] Login rechaza credenciales incorrectas
- [ ] Logout funciona correctamente
- [ ] Selección de modelo funciona
- [ ] Entrenamiento de cada modelo
- [ ] Muestra accuracy después de entrenar
- [ ] Cargar datos de ejemplo (Benigno)
- [ ] Cargar datos de ejemplo (Maligno)
- [ ] Generar datos aleatorios
- [ ] Realizar predicción
- [ ] Limpiar formulario
- [ ] Cambiar modo claro/oscuro

### Usabilidad (UX)

- [ ] Botones de acción claros y visibles
- [ ] Feedback visual durante carga
- [ ] Mensajes de error descriptivos
- [ ] Mensajes de éxito informativos
- [ ] Navegación intuitiva
- [ ] Formulario fácil de completar
- [ ] Resultados fáciles de interpretar

### Responsividad

- [ ] Layout correcto en móvil
- [ ] Layout correcto en tablet
- [ ] Layout correcto en desktop
- [ ] Botones accesibles en táctil
- [ ] Texto legible en todas las pantallas
- [ ] Formulario usable en móvil

### Accesibilidad

- [ ] Contraste de colores adecuado
- [ ] Labels en inputs
- [ ] Navegación por teclado
- [ ] Mensajes de estado claros

---

## 🔄 Casos de Prueba Detallados

### TC001: Login Exitoso
```
Precondición: Usuario no autenticado
Pasos:
1. Ingresar usuario: admin
2. Ingresar contraseña: admin
3. Clic en "Iniciar Sesión"
Resultado esperado: Acceso al panel principal
```

### TC002: Login Fallido
```
Precondición: Usuario no autenticado
Pasos:
1. Ingresar usuario: wrong
2. Ingresar contraseña: wrong
3. Clic en "Iniciar Sesión"
Resultado esperado: Mensaje de error
```

### TC003: Entrenar Random Forest
```
Precondición: Usuario autenticado
Pasos:
1. Seleccionar "Random Forest"
2. Clic en "Entrenar"
3. Esperar finalización
Resultado esperado: Mensaje de éxito con accuracy
```

### TC004: Predicción con Datos de Ejemplo
```
Precondición: Modelo entrenado
Pasos:
1. Clic en "Caso Maligno"
2. Clic en "Realizar Predicción"
Resultado esperado: Predicción "Maligno"
```

### TC005: Modo Oscuro
```
Precondición: Modo claro activo
Pasos:
1. Clic en icono de luna
Resultado esperado: Interfaz cambia a modo oscuro
```

---

## 📊 Métricas de Calidad

### Cobertura de Código
- Backend: >80%
- Frontend: >70%

### Tiempos de Respuesta
- Login: <1s
- Entrenamiento: <10s
- Predicción: <2s

### Usabilidad
- Tiempo para completar tarea: <2min
- Errores de usuario: <5%

---

## 🐛 Reporte de Bugs

### Plantilla
```markdown
**Título:** [Breve descripción]
**Severidad:** Crítico / Alto / Medio / Bajo
**Pasos para reproducir:**
1. ...
2. ...
**Resultado actual:** ...
**Resultado esperado:** ...
**Capturas:** [si aplica]
**Entorno:** [navegador, OS]
```

---

*[← Volver al Índice](./index.md)*
