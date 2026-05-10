# Tibia Wiki Boosted Scraper 🛡️🦑

Este proyecto es un scraper automatizado diseñado para **OTServers** (Open Tibia Servers). Su función principal es consultar la base de datos local para identificar la criatura y el jefe (boss) "boosted" del día y descargar sus imágenes originales directamente desde Tibia Wiki usando un navegador Chromium controlado.

## 🗺️ Mapa del Proyecto

* **Main.py**: El núcleo del programa. Gestiona la conexión a MariaDB y la lógica de navegación con Playwright.
* **monsters/**: Carpeta de destino donde se almacenan los archivos `.gif`.
* **requirements.txt**: Archivo de dependencias para una instalación rápida.

## 🚀 Características

- **Conexión MariaDB**: Obtiene automáticamente los nombres de las tablas `boosted_creature` y `boosted_boss`.
- **Bypass de Bloqueos (403)**: Utiliza **Playwright + Chromium** para imitar el comportamiento humano y evitar protecciones de Fandom/Cloudflare.
- **Control de Duplicados**: Si el archivo `.gif` ya existe en la carpeta `/monsters/`, el script salta la descarga para ahorrar recursos.
- **URLs de Alta Calidad**: Obtiene la ruta completa del archivo incluyendo revisiones para asegurar la descarga del GIF original.

## 🛠️ Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/ZeroCrazy/tibia-boosted-scraper.git
    cd tibia-boosted-scraper
    ```

2.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Instala el motor de Chromium:**
    ```bash
    playwright install chromium
    ```

## ⚙️ Configuración

Edita las credenciales de la base de datos en `Main.py` para que coincidan con tu entorno local:

```python
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "tu_password",
    "database": "tu_database"
}
