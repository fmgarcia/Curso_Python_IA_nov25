# 🚀 Guía de Despliegue en Producción

## Despliegue en VPS Contabo con Docker

Esta guía explica paso a paso cómo desplegar el Sistema de Detección de Tumores en un servidor VPS de Contabo utilizando Docker.

---

## 📋 Índice

1. [Requisitos Previos](#requisitos-previos)
2. [Configuración del VPS](#configuración-del-vps)
3. [Instalación de Docker](#instalación-de-docker)
4. [Configuración de GitHub](#configuración-de-github)
5. [Despliegue Manual](#despliegue-manual)
6. [Despliegue Automático (CI/CD)](#despliegue-automático-cicd)
7. [Configuración de SSL (HTTPS)](#configuración-de-ssl-https)
8. [Mantenimiento](#mantenimiento)
9. [Solución de Problemas](#solución-de-problemas)

---

## 📦 Requisitos Previos

### En tu máquina local
- Git instalado
- Cuenta de GitHub con el repositorio del proyecto
- (Opcional) Docker Desktop para probar localmente

### En el VPS de Contabo
- VPS con Ubuntu 22.04 LTS (recomendado)
- Mínimo 2GB RAM, 2 vCPU
- Acceso SSH configurado
- (Opcional) Dominio apuntando al VPS

---

## 🖥️ Configuración del VPS

### 1. Conectarse al VPS

```bash
ssh root@TU_IP_VPS
```

### 2. Actualizar el sistema

```bash
apt update && apt upgrade -y
```

### 3. Crear usuario no-root (recomendado)

```bash
# Crear usuario
adduser deploy

# Añadir a grupo sudo
usermod -aG sudo deploy

# Cambiar a usuario deploy
su - deploy
```

### 4. Configurar SSH con clave pública (opcional pero recomendado)

En tu máquina local:
```bash
# Generar clave SSH si no tienes una
ssh-keygen -t ed25519 -C "tu_email@ejemplo.com"

# Copiar clave al servidor
ssh-copy-id deploy@TU_IP_VPS
```

### 5. Configurar firewall

```bash
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

---

## 🐳 Instalación de Docker

### 1. Instalar Docker

```bash
# Instalar dependencias
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Añadir clave GPG de Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Añadir repositorio
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
```

### 2. Instalar Docker Compose

```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### 3. Configurar Docker para usuario no-root

```bash
sudo usermod -aG docker $USER
newgrp docker
```

### 4. Verificar instalación

```bash
docker --version
docker-compose --version
```

---

## 🔧 Configuración de GitHub

### 1. Subir proyecto a GitHub

En tu máquina local:
```bash
cd C:\Users\Fran\Documents\EOI2025\06_IA\Curso_Python_IA_nov25\Proyecto_completo

# Inicializar Git si no está
git init

# Añadir archivos
git add .

# Commit
git commit -m "Configuración Docker para producción"

# Añadir remoto (reemplazar con tu repositorio)
git remote add origin https://github.com/TU_USUARIO/tumor-detection.git

# Push
git push -u origin main
```

### 2. Crear .gitignore (si no existe)

```gitignore
# Python
__pycache__/
*.py[cod]
venv/
.env

# Node
node_modules/
build/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Weights (opcional - puedes querer incluirlos)
# backend/weights/*.joblib

# Logs
*.log
```

---

## 🚀 Despliegue Manual

### 1. Clonar repositorio en el VPS

```bash
# Crear directorio de aplicaciones
sudo mkdir -p /opt/tumor-detection
sudo chown $USER:$USER /opt/tumor-detection

# Clonar repositorio
cd /opt/tumor-detection
git clone https://github.com/TU_USUARIO/tumor-detection.git .
```

### 2. Construir y ejecutar con Docker Compose

```bash
# Construir imágenes
docker-compose build

# Iniciar servicios en segundo plano
docker-compose up -d
```

### 3. Verificar que todo funciona

```bash
# Ver contenedores corriendo
docker-compose ps

# Ver logs
docker-compose logs -f

# Probar backend
curl http://localhost:8000/

# Probar frontend
curl http://localhost/
```

### 4. Acceder a la aplicación

Abre en el navegador: `http://TU_IP_VPS`

---

## 🔄 Despliegue Automático (CI/CD)

### Opción A: GitHub Actions (Recomendado)

#### 1. Configurar Secrets en GitHub

Ve a tu repositorio → Settings → Secrets and variables → Actions

Añadir los siguientes secrets:

| Secret | Descripción |
|--------|-------------|
| `VPS_HOST` | IP de tu VPS (ej: `123.45.67.89`) |
| `VPS_USER` | Usuario SSH (ej: `deploy`) |
| `VPS_SSH_KEY` | Clave privada SSH completa |

#### 2. Obtener la clave SSH privada

En tu máquina local:
```bash
cat ~/.ssh/id_ed25519
```

Copia todo el contenido (incluyendo `-----BEGIN...` y `-----END...`)

#### 3. Configurar el VPS para recibir despliegues

En el VPS:
```bash
# Crear directorio
sudo mkdir -p /opt/tumor-detection
sudo chown deploy:deploy /opt/tumor-detection

# Clonar repositorio
cd /opt/tumor-detection
git clone https://github.com/TU_USUARIO/tumor-detection.git .

# Primera construcción
docker-compose build
docker-compose up -d
```

#### 4. Probar el pipeline

Haz un push a la rama `main`:
```bash
git add .
git commit -m "Trigger deploy"
git push origin main
```

Ve a GitHub → Actions para ver el progreso.

---

### Opción B: Webhook manual

#### 1. Crear script de deploy en el VPS

```bash
sudo nano /opt/tumor-detection/deploy.sh
```

Contenido:
```bash
#!/bin/bash
cd /opt/tumor-detection
git pull origin main
docker-compose build
docker-compose down
docker-compose up -d
docker image prune -f
echo "Deploy completado: $(date)"
```

```bash
chmod +x /opt/tumor-detection/deploy.sh
```

#### 2. Ejecutar manualmente cuando sea necesario

```bash
/opt/tumor-detection/deploy.sh
```

---

## 🔒 Configuración de SSL (HTTPS)

### Requisitos
- Dominio configurado apuntando a la IP del VPS
- Puerto 80 y 443 abiertos

### 1. Configurar dominio en archivos

Editar `nginx-proxy.conf` y reemplazar `TU_DOMINIO.com` con tu dominio real.

### 2. Obtener certificado SSL con Certbot

```bash
# Crear directorios para Certbot
mkdir -p certbot/conf certbot/www

# Obtener certificado (primera vez)
docker-compose -f docker-compose.prod.yml run --rm certbot certonly --webroot --webroot-path=/var/www/certbot -d TU_DOMINIO.com -d www.TU_DOMINIO.com --email tu@email.com --agree-tos --no-eff-email
```

### 3. Iniciar con SSL

```bash
# Usar docker-compose de producción con SSL
docker-compose -f docker-compose.prod.yml up -d
```

### 4. Renovación automática de certificados

El certificado se renueva automáticamente cada 12 horas gracias al contenedor de Certbot.

---

## 🛠️ Mantenimiento

### Comandos útiles

```bash
# Ver estado de contenedores
docker-compose ps

# Ver logs en tiempo real
docker-compose logs -f

# Ver logs de un servicio específico
docker-compose logs -f backend
docker-compose logs -f frontend

# Reiniciar servicios
docker-compose restart

# Parar todo
docker-compose down

# Reconstruir e iniciar
docker-compose up -d --build

# Limpiar imágenes no usadas
docker image prune -f

# Limpiar todo (¡cuidado!)
docker system prune -a
```

### Actualizar la aplicación

```bash
cd /opt/tumor-detection

# Actualizar código
git pull origin main

# Reconstruir y reiniciar
docker-compose up -d --build
```

### Backup de datos

```bash
# Backup de volúmenes
docker run --rm -v tumor-detection-weights:/data -v $(pwd):/backup alpine tar cvf /backup/weights-backup.tar /data

# Backup de uploads
docker run --rm -v tumor-detection-uploads:/data -v $(pwd):/backup alpine tar cvf /backup/uploads-backup.tar /data
```

### Restaurar backup

```bash
# Restaurar weights
docker run --rm -v tumor-detection-weights:/data -v $(pwd):/backup alpine tar xvf /backup/weights-backup.tar -C /

# Restaurar uploads
docker run --rm -v tumor-detection-uploads:/data -v $(pwd):/backup alpine tar xvf /backup/uploads-backup.tar -C /
```

---

## ❗ Solución de Problemas

### El contenedor no inicia

```bash
# Ver logs detallados
docker-compose logs backend
docker-compose logs frontend

# Verificar que los puertos no están en uso
sudo netstat -tlnp | grep -E '80|8000'
```

### Error de permisos

```bash
# Dar permisos al usuario actual
sudo chown -R $USER:$USER /opt/tumor-detection
```

### Error de memoria

```bash
# Ver uso de memoria
free -h
docker stats

# Aumentar swap si es necesario
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Certificado SSL no funciona

```bash
# Verificar que el dominio apunta correctamente
dig TU_DOMINIO.com

# Renovar certificado manualmente
docker-compose -f docker-compose.prod.yml run --rm certbot renew --force-renewal
```

### Frontend no conecta con Backend

```bash
# Verificar que backend está corriendo
docker-compose ps
curl http://localhost:8000/

# Verificar red Docker
docker network inspect tumor-detection-network
```

---

## 📊 Estructura de Archivos Docker

```
Proyecto_completo/
├── backend/
│   ├── Dockerfile          # Imagen del backend
│   ├── .dockerignore       # Archivos a ignorar
│   └── ...
├── frontend/
│   ├── Dockerfile          # Imagen del frontend (multi-stage)
│   ├── nginx.conf          # Config de Nginx interno
│   └── .dockerignore       # Archivos a ignorar
├── docker-compose.yml      # Compose básico (sin SSL)
├── docker-compose.prod.yml # Compose con SSL
├── nginx-proxy.conf        # Config de proxy con SSL
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions CI/CD
└── docs/
    └── despliegue.md       # Esta documentación
```

---

## 📞 Recursos Adicionales

- [Documentación de Docker](https://docs.docker.com/)
- [Documentación de Docker Compose](https://docs.docker.com/compose/)
- [Contabo VPS](https://contabo.com/)
- [Let's Encrypt](https://letsencrypt.org/)
- [GitHub Actions](https://docs.github.com/en/actions)

---

*[← Volver al Índice](./index.md)*
