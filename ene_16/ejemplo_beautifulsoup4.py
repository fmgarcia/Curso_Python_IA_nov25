from bs4 import BeautifulSoup
import requests
import csv
import time
import random

# Librerías avanzadas para bypassing
try:
    import cloudscraper
    CLOUDSCRAPER_DISPONIBLE = True
except ImportError:
    CLOUDSCRAPER_DISPONIBLE = False
    print("⚠ cloudscraper no disponible. Instala con: pip install cloudscraper")

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    SELENIUM_DISPONIBLE = True
except ImportError:
    SELENIUM_DISPONIBLE = False
    print("⚠ selenium no disponible. Instala con: pip install selenium")


def obtener_headers_navegador():
    """
    Genera headers HTTP que simulan un navegador Chrome real.
    
    Returns:
        dict: Diccionario con headers HTTP
    """
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Sec-Ch-Ua': '"Not A(Brand";v="8", "Chromium";v="131", "Google Chrome";v="131"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Referer': 'https://www.google.com/'
    }


def configurar_opciones_selenium():
    """
    Configura las opciones de Selenium para evadir detección de bots.
    
    Returns:
        Options: Objeto Options configurado para Chrome
    """
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
    return options


def obtener_html_con_cloudscraper(url):
    """
    Obtiene HTML usando CloudScraper para bypassing de Cloudflare.
    
    Args:
        url (str): URL de la página a obtener
        
    Returns:
        BeautifulSoup: HTML parseado
        
    Raises:
        Exception: Si hay error en la petición
    """
    print("🔧 Usando CloudScraper para bypassing avanzado...")
    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True
        },
        delay=10
    )
    
    time.sleep(random.uniform(2, 4))
    
    response = scraper.get(url, timeout=30)
    response.raise_for_status()
    
    print("✓ Petición exitosa con CloudScraper")
    return BeautifulSoup(response.text, 'html.parser')


def obtener_html_con_selenium(url):
    """
    Obtiene HTML usando Selenium (navegador real automatizado).
    
    Args:
        url (str): URL de la página a obtener
        
    Returns:
        BeautifulSoup: HTML parseado
        
    Raises:
        Exception: Si hay error en la petición
    """
    print("🌐 Usando Selenium (navegador real)...")
    
    options = configurar_opciones_selenium()
    driver = webdriver.Chrome(options=options)
    
    # Modificar propiedades para evadir detección
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    print(f"Navegando a {url}...")
    driver.get(url)
    
    time.sleep(random.uniform(3, 6))
    
    # Esperar a que aparezcan las tarjetas de coches
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "mt-CardAd"))
        )
        print("✓ Contenido cargado")
    except:
        print("⚠ Timeout esperando contenido, continuando...")
    
    html = driver.page_source
    driver.quit()
    
    print("✓ Petición exitosa con Selenium")
    return BeautifulSoup(html, 'html.parser')


def obtener_html_con_requests(url):
    """
    Obtiene HTML usando requests estándar con headers mejorados.
    
    Args:
        url (str): URL de la página a obtener
        
    Returns:
        BeautifulSoup: HTML parseado
        
    Raises:
        Exception: Si hay error en la petición
    """
    print("📡 Usando requests estándar con headers mejorados...")
    
    session = requests.Session()
    headers = obtener_headers_navegador()
    
    # Visitar la página principal primero
    print("Visitando página principal...")
    home_response = session.get('https://www.coches.net/', headers=headers, timeout=15)
    home_response.raise_for_status()
    
    time.sleep(random.uniform(2, 4))
    
    # Actualizar headers para simular navegación interna
    headers['Referer'] = 'https://www.coches.net/'
    headers['Sec-Fetch-Site'] = 'same-origin'
    
    print("Realizando petición principal...")
    response = session.get(url, headers=headers, timeout=15, allow_redirects=True)
    response.raise_for_status()
    
    print("✓ Petición exitosa con requests")
    return BeautifulSoup(response.text, 'html.parser')


def obtener_html(url, metodo='cloudscraper'):
    """
    Realiza una petición HTTP y devuelve el contenido HTML parseado.
    Soporta múltiples métodos para evadir protecciones anti-bot.
    
    Args:
        url (str): URL de la página a obtener
        metodo (str): Método a usar: 'cloudscraper', 'selenium', o 'requests'
        
    Returns:
        BeautifulSoup: Objeto BeautifulSoup con el HTML parseado
        
    Raises:
        requests.exceptions.RequestException: Si hay error en la petición HTTP
    """
    # MÉTODO 1: CloudScraper (Mejor para Cloudflare)
    if metodo == 'cloudscraper' and CLOUDSCRAPER_DISPONIBLE:
        try:
            return obtener_html_con_cloudscraper(url)
        except Exception as e:
            print(f"❌ Error con CloudScraper: {e}")
            if SELENIUM_DISPONIBLE:
                print("Intentando con Selenium...")
                return obtener_html(url, metodo='selenium')
            raise
    
    # MÉTODO 2: Selenium (Navegador real)
    elif metodo == 'selenium' and SELENIUM_DISPONIBLE:
        try:
            return obtener_html_con_selenium(url)
        except Exception as e:
            print(f"❌ Error con Selenium: {e}")
            raise
    
    # MÉTODO 3: Requests estándar (fallback)
    else:
        if metodo == 'cloudscraper' and not CLOUDSCRAPER_DISPONIBLE:
            print("⚠ CloudScraper no disponible, usando requests estándar")
        elif metodo == 'selenium' and not SELENIUM_DISPONIBLE:
            print("⚠ Selenium no disponible, usando requests estándar")
        
        try:
            return obtener_html_con_requests(url)
        except Exception as e:
            print(f"❌ Error con requests: {e}")
            raise


def extraer_descripcion(tarjeta):
    """
    Extrae la descripción del coche de una tarjeta.
    
    Args:
        tarjeta: Elemento BeautifulSoup de la tarjeta del coche
        
    Returns:
        str: Descripción del coche o 'N/A' si no se encuentra
    """
    descripcion_tag = tarjeta.find('a', class_='mt-CardAd-infoHeaderTitleLink')
    return descripcion_tag.text.strip() if descripcion_tag else 'N/A'


def extraer_precio(tarjeta):
    """
    Extrae el precio del coche de una tarjeta.
    
    Args:
        tarjeta: Elemento BeautifulSoup de la tarjeta del coche
        
    Returns:
        str: Precio del coche o 'N/A' si no se encuentra
    """
    precio_tag = tarjeta.find('p', class_='mt-CardAdPrice-cashAmount')
    return precio_tag.text.strip() if precio_tag else 'N/A'


def extraer_atributos(tarjeta):
    """
    Extrae año y kilómetros de los atributos de la tarjeta.
    
    Args:
        tarjeta: Elemento BeautifulSoup de la tarjeta del coche
        
    Returns:
        tuple: (año, kilometros) como strings, 'N/A' si no se encuentran
    """
    atributos = tarjeta.find_all('li', class_='mt-CardAd-attrItem')
    
    año = 'N/A'
    kilometros = 'N/A'
    
    for atributo in atributos:
        texto = atributo.text.strip()
        # Detectar año (4 dígitos)
        if texto.isdigit() and len(texto) == 4:
            año = texto
        # Detectar kilómetros (contiene 'km')
        elif 'km' in texto.lower():
            kilometros = texto
    
    return año, kilometros


def extraer_datos_tarjeta(tarjeta):
    """
    Extrae todos los datos relevantes de una tarjeta de coche.
    
    Args:
        tarjeta: Elemento BeautifulSoup de la tarjeta del coche
        
    Returns:
        dict: Diccionario con los datos del coche (Descripción, Precio, Año, Kilómetros)
    """
    descripcion = extraer_descripcion(tarjeta)
    precio = extraer_precio(tarjeta)
    año, kilometros = extraer_atributos(tarjeta)
    
    return {
        'Descripción': descripcion,
        'Precio': precio,
        'Año': año,
        'Kilómetros': kilometros
    }


def obtener_tarjetas_coches(soup):
    """
    Encuentra y devuelve todas las tarjetas de coches en el HTML.
    
    Args:
        soup: Objeto BeautifulSoup con el HTML parseado
        
    Returns:
        list: Lista de elementos BeautifulSoup con las tarjetas de coches
    """
    return soup.find_all('article', class_='mt-CardAd')


def procesar_tarjetas(tarjetas):
    """
    Procesa todas las tarjetas de coches y extrae sus datos.
    
    Args:
        tarjetas: Lista de elementos BeautifulSoup con las tarjetas
        
    Returns:
        list: Lista de diccionarios con los datos de cada coche
    """
    coches = []
    
    for tarjeta in tarjetas:
        try:
            datos_coche = extraer_datos_tarjeta(tarjeta)
            coches.append(datos_coche)
        except Exception as e:
            print(f"Error al procesar una tarjeta: {e}")
            continue
    
    return coches


def guardar_en_csv(coches, nombre_archivo_csv):
    """
    Guarda la lista de coches en un archivo CSV.
    
    Args:
        coches (list): Lista de diccionarios con los datos de los coches
        nombre_archivo_csv (str): Nombre del archivo CSV donde guardar los datos
        
    Returns:
        bool: True si se guardó correctamente, False si no había datos
    """
    if not coches:
        print("No se encontraron datos para guardar")
        return False
    
    with open(nombre_archivo_csv, 'w', newline='', encoding='utf-8') as csvfile:
        campos = ['Descripción', 'Precio', 'Año', 'Kilómetros']
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        
        writer.writeheader()
        writer.writerows(coches)
    
    print(f"✓ Datos guardados exitosamente en '{nombre_archivo_csv}'")
    print(f"✓ Total de coches extraídos: {len(coches)}")
    return True


def extraer_coches_a_csv(url, nombre_archivo_csv, metodo='cloudscraper'):
    """
    Extrae información de coches desde coches.net y la guarda en un archivo CSV.
    
    Args:
        url (str): URL de la página de búsqueda en coches.net
        nombre_archivo_csv (str): Nombre del archivo CSV donde se guardarán los datos
        metodo (str): Método de scraping: 'cloudscraper' (defecto), 'selenium', o 'requests'
    """
    try:
        # Obtener y parsear el HTML
        soup = obtener_html(url, metodo=metodo)
        
        # Encontrar todas las tarjetas de coches
        tarjetas = obtener_tarjetas_coches(soup)
        print(f"Se encontraron {len(tarjetas)} coches")
        
        # Procesar las tarjetas y extraer datos
        coches = procesar_tarjetas(tarjetas)
        
        # Guardar en CSV
        guardar_en_csv(coches, nombre_archivo_csv)
            
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición HTTP: {e}")
    except Exception as e:
        print(f"Error general: {e}")


# Ejemplo de uso
if __name__ == "__main__":
    url_ejemplo = "https://www.coches.net/search/?hasPhoto=false&wwa=false&MakeIds%5B0%5D=7&ModelIds%5B0%5D=70"
    archivo_salida = "./ficheros/coches_bmw_serie3.csv"
    
    print(f"Extrayendo datos de: {url_ejemplo}")
    print("\nMétodos disponibles:")
    print("  1. 'cloudscraper' - Bypassing avanzado de Cloudflare (RECOMENDADO)")
    print("  2. 'selenium' - Navegador real automatizado (MUY EFECTIVO)")
    print("  3. 'requests' - Peticiones HTTP estándar (básico)")
    print()
    
    # Intenta primero con cloudscraper, luego selenium, finalmente requests
    extraer_coches_a_csv(url_ejemplo, archivo_salida, metodo='selenium')

