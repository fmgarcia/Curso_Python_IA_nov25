# 🔧 Guía de Instalación

## Requisitos Previos

### Sistema Operativo
- Windows 10/11, macOS, o Linux

### Software Necesario
- **Python** 3.11 o superior
- **Node.js** 18.x o superior
- **npm** 9.x o superior
- **Git** (opcional, para clonar)

---

## 📦 Instalación del Backend

### 1. Navegar al directorio del backend

```powershell
cd C:\Users\Fran\Documents\EOI2025\06_IA\Curso_Python_IA_nov25\Proyecto_completo\backend
```

### 2. Crear entorno virtual

```powershell
python -m venv venv
```

### 3. Activar entorno virtual

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.\venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```powershell
pip install -r requirements.txt
```

### 5. Verificar instalación

```powershell
python -c "import fastapi; import sklearn; print('OK')"
```

---

## 🎨 Instalación del Frontend

### 1. Navegar al directorio del frontend

```powershell
cd C:\Users\Fran\Documents\EOI2025\06_IA\Curso_Python_IA_nov25\Proyecto_completo\frontend
```

### 2. Instalar dependencias

```powershell
npm install
```

### 3. Verificar instalación

```powershell
npm list react
```

---

## 🚀 Ejecutar la Aplicación

### Iniciar Backend

```powershell
cd backend
.\venv\Scripts\Activate.ps1
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

El backend estará disponible en: `http://localhost:8000`

### Iniciar Frontend

En otra terminal:
```powershell
cd frontend
npm start
```

El frontend estará disponible en: `http://localhost:3000`

---

## ✅ Verificación

### Backend
Abrir en navegador: `http://localhost:8000/docs`

Debe mostrar la documentación Swagger de la API.

### Frontend
Abrir en navegador: `http://localhost:3000`

Debe mostrar la pantalla de login.

---

## 🔧 Solución de Problemas

### Error: Puerto 8000 en uso

```powershell
# Encontrar proceso usando el puerto
netstat -ano | findstr :8000

# Terminar proceso
taskkill /F /PID <PID>
```

### Error: Módulo no encontrado

```powershell
# Reinstalar dependencias
pip install -r requirements.txt --force-reinstall
```

### Error: npm install falla

```powershell
# Limpiar caché
npm cache clean --force
rm -rf node_modules
npm install
```

### Error: CORS

Verificar que el frontend esté corriendo en `http://localhost:3000` (no en otro puerto).

---

## 📋 Dependencias

### requirements.txt (Backend)
```
fastapi==0.109.0
uvicorn==0.27.0
scikit-learn==1.4.0
xgboost==2.0.3
pandas==2.2.0
numpy==1.26.3
joblib==1.3.2
python-multipart==0.0.6
```

### package.json (Frontend)
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "axios": "^1.6.0"
  }
}
```

---

*[← Volver al Índice](./index.md)*
