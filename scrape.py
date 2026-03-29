import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime

URL = "https://www.oem-ag.at/marktpreis/"
SELECTOR = "table.table-bordered > tbody > tr:last-child > td:nth-child(2)"

def main():
    try:
        # 1. Webseite abrufen
        headers = {'User-Agent': 'Mozilla/5.0'} 
        response = requests.get(URL, headers=headers)
        response.raise_for_status()
        
        # 2. HTML parsen und Element finden
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.select_one(SELECTOR)
        
        if price_element:
            raw_text = price_element.text.strip()
            
            # 3. Wert bereinigen und umrechnen (wie in deinem value_template)
            # Finde alle Ziffern und Kommas: regex_findall_index("[\d,]+")
            match = re.search(r'[\d,]+', raw_text)
            
            if match:
                # Komma durch Punkt ersetzen und als Float einlesen
                number_str = match.group(0).replace(',', '.')
                # float(0) / 100
                price_eur = float(number_str) / 100
                
                # 4. JSON Datenstruktur aufbauen
                data = {
                    "timestamp": datetime.now().isoformat(),
                    "oemag_marktpreis": price_eur,
                    "unit": "EUR/kWh",
                    "raw_scraped_value": raw_text
                }
                
                # 5. In preis.json speichern
                with open("preis.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                    
                print(f"Erfolgreich gespeichert: {data}")
            else:
                print(f"Fehler: Konnte im Text '{raw_text}' keine Zahl finden.")
        else:
            print(f"Fehler: Das Element mit dem Selektor '{SELECTOR}' wurde nicht gefunden.")
            
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()