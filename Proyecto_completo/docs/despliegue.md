# 🚀 Guía de Despliegue en Producción

## Despliegue en Contabo VPS con Dokploy

Esta guía explica paso a paso cómo desplegar el Sistema de Detección de Tumores en un servidor VPS de Contabo utilizando **Dokploy** como plataforma de despliegue.

---

## 📋 Índice

1. [Arquitectura del Despliegue](#1-arquitectura-del-despliegue)
2. [Requisitos Previos](#2-requisitos-previos)
3. [Estructura del Repositorio](#3-estructura-del-repositorio)
4. [Configuración de Dokploy](#4-configuración-de-dokploy)
5. [Crear la Aplicación en Dokploy](#5-crear-la-aplicación-en-dokploy)
6. [Configuración del Compose](#6-configuración-del-compose)
7. [Primer Despliegue](#7-primer-despliegue)
8. [Configurar Dominio y SSL](#8-configurar-dominio-y-ssl)
9. [Despliegue Automático (CI/CD)](#9-despliegue-automático-cicd)
10. [Mantenimiento y Monitorización](#10-mantenimiento-y-monitorización)
11. [Solución de Problemas](#11-solución-de-problemas)

---

## 1. Arquitectura del Despliegue

```
┌──────────────────────────────────────────────────────────┐
│                    VPS CONTABO                           │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │                  DOKPLOY                           │  │
│  │                                                    │  │
│  │  ┌─────────┐    ┌──────────────────────────────┐  │  │
│  │  │ Traefik │    │  App: detecciontumores       │  │  │
│  │  │ (proxy) │───►│                              │  │  │
│  │  │  :80    │    │  ┌──────────┐  ┌──────────┐  │  │  │
│  │  │  :443   │    │  │ Frontend │  │ Backend  │  │  │  │
│  │  └─────────┘    │  │  Nginx   │─►│ FastAPI  │  │  │  │
│  │                 │  │   :80    │  │  :8000   │  │  │  │
│  │                 │  └──────────┘  └──────────┘  │  │  │
│  │                 │                              │  │  │
│  │                 │  Volumes:                    │  │  │
│  │                 │  - weights/ (modelos ML)     │  │  │
│  │                 │  - uploads/ (datasets)       │  │  │
│  │                 └──────────────────────────────┘  │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

### ¿Por qué Dokploy?

- **Interfaz web** para gestionar despliegues (sin SSH manual)
- **SSL automático** con Let's Encrypt vía Traefik
- **Despliegue desde GitHub** con un clic o webhook
- **Monitorización** de contenedores integrada
- **Logs** accesibles desde la interfaz
- **Rollback** fácil a versiones anteriores

---

## 2. Requisitos Previos

### En tu máquina local (Windows)
- ✅ Git instalado
- ✅ Proyecto subido a GitHub
- ✅ Node.js y Python (para desarrollo local)

### En el VPS de Contabo
- ✅ VPS con Ubuntu 22.04 LTS
- ✅ Mínimo 2GB RAM, 2 vCPU
- ✅ **Dokploy instalado y funcionando**
- ✅ Acceso al panel de Dokploy (ej: `http://TU_IP_VPS:3000`)

### Repositorio GitHub
- ✅ URL: `https://github.com/fmgarcia/Curso_Python_IA_nov25`
- ✅ El proyecto está en la subcarpeta `Proyecto_completo/`

---

## 3. Estructura del Repositorio

El repositorio de GitHub tiene la siguiente estructura. Es importante entender que el proyecto **no está en la raíz** del repositorio, sino dentro de `Proyecto_completo/`:

```
Curso_Python_IA_nov25/              ← Raíz del repositorio en GitHub
├── otros_archivos/                 ← Otros contenidos del curso
├── ...
└── Proyecto_completo/              ← ★ AQUÍ ESTÁ EL PROYECTO ★
    ├── docker-compose.yml          ← Orquestación Docker
    ├── .gitignore
    ├── backend/
    │   ├── Dockerfile              ← Imagen del backend
    │   ├── .dockerignore
    │   ├── main.py
    │   ├── requirements.txt
    │   ├── models/
    │   ├── weights/
    │   └── uploads/
    ├── frontend/
    │   ├── Dockerfile              ← Imagen del frontend (multi-stage)
    │   ├── .dockerignore
    │   ├── nginx.conf              ← Config Nginx interna
    │   ├── package.json
    │   └── src/
    ├── docs/
    │   └── despliegue.md           ← Este documento
    └── .github/
        └── workflows/
            └── deploy.yml          ← CI/CD con GitHub Actions
```

---

## 4. Configuración de Dokploy

### 4.1. Instalar Dokploy (si no está instalado)

Conectarse al VPS por SSH:

```bash
ssh root@TU_IP_VPS
```

Instalar Dokploy:

```bash
curl -sSL https://dokploy.com/install.sh | sh
```

Una vez instalado, acceder al panel en: `http://TU_IP_VPS:3000`

### 4.2. Primer acceso

1. Abrir `http://TU_IP_VPS:3000` en el navegador
2. Crear cuenta de administrador (primera vez)
3. Acceder al dashboard de Dokploy

---

## 5. Crear la Aplicación en Dokploy

### 5.1. Crear nuevo proyecto

1. En el dashboard de Dokploy, clic en **"Projects"** → **"Create Project"**
2. Nombre del proyecto: `detecciontumores`
3. Clic en **"Create"**

### 5.2. Crear aplicación de tipo Compose

1. Dentro del proyecto `detecciontumores`, clic en **"+ Create Service"**
2. Seleccionar **"Compose"**
3. Nombre: `detecciontumores`

### 5.3. Conectar con GitHub

1. En la configuración de la aplicación, ir a la pestaña **"General"**
2. En **Provider**, seleccionar **"GitHub"**
3. Si no está conectado, autorizar Dokploy en tu cuenta de GitHub
4. Configurar:

| Campo | Valor |
|-------|-------|
| **Repository** | `fmgarcia/Curso_Python_IA_nov25` |
| **Branch** | `main` |
| **Compose Path** | `./Proyecto_completo/docker-compose.yml` |

> ⚠️ **MUY IMPORTANTE**: El campo **Compose Path** debe apuntar a `./Proyecto_completo/docker-compose.yml` ya que el proyecto no está en la raíz del repositorio.

---

## 6. Configuración del Compose

### 6.1. Entender el docker-compose.yml

El archivo `docker-compose.yml` define dos servicios:

```yaml
services:
  backend:          # FastAPI en puerto 8000
  frontend:         # React + Nginx en puerto 80
```

### 6.2. Contexto de Build

Dado que Dokploy clona todo el repositorio y el `docker-compose.yml` está en `Proyecto_completo/`, los paths de build context son **relativos a esa subcarpeta**:

```yaml
services:
  backend:
    build:
      context: ./backend        # → Proyecto_completo/backend/
      dockerfile: Dockerfile
  frontend:
    build:
      context: ./frontend       # → Proyecto_completo/frontend/
      dockerfile: Dockerfile
```

### 6.3. Red de Dokploy

El compose usa la red de Dokploy para que Traefik pueda enrutar tráfico:

```yaml
networks:
  dokploy-network:
    external: true
```

### 6.4. Volúmenes Persistentes

Los modelos entrenados y datasets subidos se persisten en volúmenes Docker:

```yaml
volumes:
  backend_weights:    # Modelos .joblib entrenados
  backend_uploads:    # Datasets CSV personalizados
```

---

## 7. Primer Despliegue

### 7.1. Desplegar

1. En Dokploy, ir a la aplicación `detecciontumores`
2. Pestaña **"Deployments"**
3. Clic en **"Deploy"**
4. Esperar a que se construyan ambas imágenes (puede tardar 3-5 min la primera vez)

### 7.2. Verificar despliegue

1. En la pestaña **"Deployments"**, verificar que el estado es ✅ **"Running"**
2. Clic en **"Logs"** para ver los logs de cada contenedor
3. Verificar en los logs del backend:
   ```
   INFO:     Uvicorn running on http://0.0.0.0:8000
   ```
4. Verificar en los logs del frontend que Nginx ha arrancado

### 7.3. Probar la aplicación

Si aún no tienes dominio configurado, puedes verificar por SSH:

```bash
ssh root@TU_IP_VPS

# Probar backend
docker exec detecciontumores-backend curl -s http://localhost:8000/
# Debe devolver JSON con info de la API

# Probar frontend
docker exec detecciontumores-frontend wget -qO- http://localhost:80/ | head -5
# Debe devolver HTML
```

---

## 8. Configurar Dominio y SSL

### 8.1. Configurar DNS

En tu proveedor de dominio, crear un registro **A** que apunte a la IP del VPS:

| Tipo | Nombre | Valor |
|------|--------|-------|
| A | `tumores` | `TU_IP_VPS` |
| A | `www.tumores` | `TU_IP_VPS` |

Ejemplo: si tu dominio es `midominio.com`, el subdominio sería `tumores.midominio.com`

### 8.2. Configurar dominio en Dokploy

1. En la aplicación `detecciontumores`, ir a pestaña **"Domains"**
2. Clic en **"Add Domain"**
3. Configurar:

| Campo | Valor |
|-------|-------|
| **Host** | `tumores.midominio.com` (tu dominio real) |
| **Container Port** | `80` |
| **Service Name** | `frontend` |
| **HTTPS** | ✅ Activar |
| **Certificate** | `Let's Encrypt` |

4. Clic en **"Save"**

### 8.3. Verificar SSL

1. Esperar 1-2 minutos a que Traefik obtenga el certificado
2. Abrir `https://tumores.midominio.com` en el navegador
3. Verificar el candado 🔒 en la barra de direcciones
4. Debe aparecer la pantalla de login de la aplicación

> **Nota:** Dokploy gestiona la renovación automática del certificado SSL a través de Traefik. No necesitas configurar Certbot manualmente.

---

## 9. Despliegue Automático (CI/CD)

### Opción A: Webhook de Dokploy (Recomendado)

Cada push a `main` disparará automáticamente un redespliegue.

#### 9.1. Obtener el Webhook URL

1. En Dokploy, ir a la aplicación `detecciontumores`
2. Pestaña **"Deployments"**
3. Buscar la sección **"Webhook"** o **"Auto Deploy"**
4. Copiar la **Webhook URL** (tiene este formato):
   ```
   https://TU_IP_VPS:3000/api/deploy/compose/XXXXX
   ```

#### 9.2. Configurar Secret en GitHub

1. Ir a `https://github.com/fmgarcia/Curso_Python_IA_nov25/settings/secrets/actions`
2. Clic en **"New repository secret"**
3. Configurar:

| Campo | Valor |
|-------|-------|
| **Name** | `DOKPLOY_WEBHOOK_URL` |
| **Secret** | La URL del webhook copiada en el paso anterior |

#### 9.3. Probar el CI/CD

1. Hacer un cambio en cualquier archivo dentro de `Proyecto_completo/`
2. Commit y push:
   ```bash
   git add .
   git commit -m "Test CI/CD con Dokploy"
   git push origin main
   ```
3. Ir a GitHub → **Actions** → Verificar que el workflow se ejecuta
4. Ir a Dokploy → **Deployments** → Verificar que se inicia un nuevo despliegue

#### 9.4. Pipeline completo

El flujo CI/CD es el siguiente:

```
Push a main (en carpeta Proyecto_completo/)
    ↓
GitHub Actions: Job "test"
    ├── Checkout código
    ├── Instalar Python 3.11
    ├── Instalar dependencias backend
    └── Verificar que el backend importa correctamente
    ↓
GitHub Actions: Job "deploy"
    └── curl POST al webhook de Dokploy
    ↓
Dokploy (en Contabo VPS)
    ├── Pull del repositorio
    ├── Build de imágenes Docker
    ├── Detener contenedores antiguos
    └── Iniciar contenedores nuevos
    ↓
✅ Aplicación actualizada
```

---

### Opción B: Auto Deploy en Dokploy

Si prefieres no usar GitHub Actions:

1. En Dokploy, pestaña **"General"** de la aplicación
2. Activar **"Auto Deploy"**
3. Cada push a la rama `main` disparará automáticamente un redespliegue

> **Nota:** Con esta opción no se ejecutan los tests antes de desplegar.

---

## 10. Mantenimiento y Monitorización

### 10.1. Ver Logs

Desde el panel de Dokploy:

1. Ir a la aplicación `detecciontumores`
2. Pestaña **"Logs"**
3. Seleccionar el servicio: `backend` o `frontend`
4. Los logs se muestran en tiempo real

Desde SSH (alternativa):

```bash
# Logs de todos los servicios
docker logs detecciontumores-backend --tail 100 -f
docker logs detecciontumores-frontend --tail 100 -f
```

### 10.2. Monitorización de recursos

Desde Dokploy:

1. Pestaña **"Monitoring"** en la aplicación
2. Muestra uso de CPU, RAM y red de cada contenedor

Desde SSH:

```bash
# Estado de contenedores
docker ps

# Recursos en tiempo real
docker stats detecciontumores-backend detecciontumores-frontend

# Espacio en disco
df -h
```

### 10.3. Redesplegar manualmente

1. Dokploy → Aplicación → Pestaña **"Deployments"**
2. Clic en **"Deploy"**

### 10.4. Rollback a versión anterior

1. Dokploy → Aplicación → Pestaña **"Deployments"**
2. En el historial de despliegues, seleccionar uno anterior
3. Clic en **"Rollback"**

### 10.5. Backup de datos

Los modelos entrenados y datasets subidos están en volúmenes Docker:

```bash
# Conectar al VPS
ssh root@TU_IP_VPS

# Backup de modelos entrenados
docker run --rm -v detecciontumores-weights:/data \
  -v /root/backups:/backup alpine \
  tar cvf /backup/weights-$(date +%Y%m%d).tar /data

# Backup de datasets personalizados
docker run --rm -v detecciontumores-uploads:/data \
  -v /root/backups:/backup alpine \
  tar cvf /backup/uploads-$(date +%Y%m%d).tar /data
```

### 10.6. Restaurar backup

```bash
# Restaurar modelos
docker run --rm -v detecciontumores-weights:/data \
  -v /root/backups:/backup alpine \
  sh -c "cd / && tar xvf /backup/weights-YYYYMMDD.tar"

# Restaurar datasets
docker run --rm -v detecciontumores-uploads:/data \
  -v /root/backups:/backup alpine \
  sh -c "cd / && tar xvf /backup/uploads-YYYYMMDD.tar"
```

---

## 11. Solución de Problemas

### El despliegue falla en Dokploy

**Causa posible:** El Compose Path no es correcto.

```
✅ Correcto:   ./Proyecto_completo/docker-compose.yml
❌ Incorrecto: ./docker-compose.yml
❌ Incorrecto: docker-compose.yml
```

**Verificar** en Dokploy → General → Compose Path.

### Error "network dokploy-network not found"

La red `dokploy-network` debe existir. Dokploy la crea automáticamente. Si no existe:

```bash
docker network create dokploy-network
```

### El frontend no conecta con el backend

**Causa:** El frontend usa Nginx para hacer proxy de `/api/` hacia el backend.

Verificar que en `frontend/nginx.conf` el proxy apunta correctamente:

```nginx
location /api/ {
    proxy_pass http://backend:8000/;
}
```

El nombre `backend` es el nombre del servicio en `docker-compose.yml`.

**Verificar conectividad:**

```bash
# Desde dentro del contenedor frontend
docker exec detecciontumores-frontend wget -qO- http://backend:8000/
```

### Error de build en el frontend

**Causa posible:** node_modules o build incluidos en el contexto.

Verificar que `frontend/.dockerignore` incluye:

```
node_modules/
build/
```

### Error de memoria en el VPS

```bash
# Ver uso de memoria
free -h

# Crear/ampliar swap
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
# Persistir swap
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### Los modelos entrenados se pierden al redesplegar

Los modelos se guardan en el volumen Docker `detecciontumores-weights`. Si el volumen existe, los datos persisten entre redespliegues.

Verificar que el volumen existe:

```bash
docker volume ls | grep detecciontumores
```

Si se eliminó accidentalmente, restaurar desde backup (ver sección 10.6).

### Ver los archivos dentro de un contenedor

```bash
# Backend
docker exec -it detecciontumores-backend ls -la /app/weights/
docker exec -it detecciontumores-backend ls -la /app/uploads/

# Frontend
docker exec -it detecciontumores-frontend ls -la /usr/share/nginx/html/
```

---

## 📊 Resumen de Arquitectura Docker

```
Proyecto_completo/
├── docker-compose.yml          ← Orquestación (Dokploy Compose)
├── backend/
│   ├── Dockerfile              ← Python 3.11 + FastAPI
│   └── .dockerignore
├── frontend/
│   ├── Dockerfile              ← Node 18 (build) + Nginx (prod)
│   ├── nginx.conf              ← Proxy /api/ → backend:8000
│   └── .dockerignore
└── .github/
    └── workflows/
        └── deploy.yml          ← Tests + Webhook Dokploy
```

### Flujo de red en producción

```
Usuario (HTTPS)
    ↓
Traefik (Dokploy - puerto 443)
    ↓
Frontend (Nginx - puerto 80)
    ├── Archivos estáticos (React)  → /
    └── Proxy API                   → /api/ → Backend:8000
```

---

## 📞 Recursos Adicionales

- [Documentación de Dokploy](https://docs.dokploy.com/)
- [Contabo VPS](https://contabo.com/)
- [Documentación de Docker](https://docs.docker.com/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Repositorio del proyecto](https://github.com/fmgarcia/Curso_Python_IA_nov25)

---

*[← Volver al Índice](./index.md)*
