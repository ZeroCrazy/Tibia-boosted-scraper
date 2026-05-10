import mysql.connector
from playwright.sync_api import sync_playwright
import os

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "tu_password",
    "database": "tu_database"
}

def get_targets_from_db():
    targets = []
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        cursor.execute("SELECT boostname FROM boosted_creature LIMIT 1")
        row_creature = cursor.fetchone()
        if row_creature:
            targets.append(row_creature[0])
            
        cursor.execute("SELECT boostname FROM boosted_boss LIMIT 1")
        row_boss = cursor.fetchone()
        if row_boss:
            targets.append(row_boss[0])
            
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error de BD: {e}")
    return targets

def download_with_chromium(name):
    folder = "monsters"
    filename = f"{name.lower().replace(' ', '_')}.gif"
    filepath = os.path.join(folder, filename)

    if not os.path.exists(folder):
        os.makedirs(folder)

    if os.path.exists(filepath):
        print(f"[!] '{filename}' ya existe. Saltando...")
        return

    url = f"https://tibia.fandom.com/wiki/{name.replace(' ', '_')}"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        print(f"[*] Navegando a {url}...")
        try:
            page.goto(url, wait_until="networkidle")
            img_element = page.locator("#twbox-image img").first
            
            if img_element.count() > 0:
                img_url = img_element.get_attribute("src")
                print(f"[+] URL detectada: {img_url}")
                
                response = page.request.get(img_url)
                if response.status == 200:
                    with open(filepath, "wb") as f:
                        f.write(response.body())
                    print(f"[SUCCESS] Guardado: {filepath}")
            else:
                print(f"[-] No se encontró imagen para '{name}'.")
        except Exception as e:
            print(f"[-] Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    print("*** Scraper de Boosted (Creature & Boss) ***")
    targets = get_targets_from_db()
    
    if targets:
        for name in targets:
            print(f"\n[+] Procesando: {name}")
            download_with_chromium(name)
    else:
        print("[-] No se encontraron registros en ninguna tabla.")