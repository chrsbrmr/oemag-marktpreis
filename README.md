# ⚡ ÖMAG Marktpreis Scraper

Tägliche Aktualisierung des Strommarktpreises der ÖMAG.

## 📋 Überblick

Dieses Repository aktualisiert die Datei `preis.json` täglich mit dem aktuellen Marktpreis für Strom von der [ÖMAG (Abwicklungsstelle für Ökostrom AG)](https://www.oem-ag.at/).

Der Scraper ruft die Marktpreisdaten automatisch ab und speichert sie in einem strukturierten JSON-Format für die einfache Integration.

## 🎯 Funktionen

* Automatisches Scraping der ÖMAG-Website
* Tägliche Aktualisierung des Marktpreises
* Strukturierte JSON-Ausgabe mit Metadaten
* Zeitstempel zur Nachverfolgung
* Preisangaben in EUR/kWh

## 📦 Struktur

### Quelle

* 🌐 [https://www.oem-ag.at/marktpreis/](https://www.oem-ag.at/marktpreis/)

### Ausgabe

* 💾 **Datei**: `preis.json`
* 📊 **Format**: JSON mit folgendem Inhalt:
```json
{
  "timestamp": "2026-03-29T14:13:47.041157",
  "oemag_marktpreis": 0.08457,
  "unit": "EUR/kWh",
  "raw_scraped_value": "8,457 ct/kWh"
}

```



Abrufbar unter:

```
https://raw.githubusercontent.com/chrsbrmr/oemag-marktpreis/refs/heads/main/preis.json

```

## 🚀 Verwendung

### Voraussetzungen

```bash
pip install -r requirements.txt

```

### Manuelle Ausführung

```bash
python scrape.py

```

### Automatisierung

Die tägliche Ausführung erfolgt über **GitHub Actions** (`.github/workflows/scrape.yml`) automatisch nach Zeitplan.

### Home Assistant Integration

Den folgenden Eintrag in die `configuration.yaml` einfügen:

```yaml
sensor:
  - platform: rest
    name: "OeMAG Marktpreis"
    unique_id: oemag_marktpreis_github
    resource: "https://raw.githubusercontent.com/chrsbrmr/oemag-marktpreis/refs/heads/main/preis.json"
    value_template: "{{ value_json.oemag_marktpreis }}"
    unit_of_measurement: "EUR/kWh"
    device_class: monetary
    state_class: measurement
    scan_interval: 86400

```

### evcc Integration

Einbindung in evcc als Einspeisevergütung (**neue Einspeisevergütung -> benutzerdefiniertes Gerät**):

```yaml
price:
  source: http
  uri: https://raw.githubusercontent.com/chrsbrmr/oemag-marktpreis/refs/heads/main/preis.json
  jq: .oemag_marktpreis

```

## 📦 Abhängigkeiten

* `requests`
* `beautifulsoup4`

## 🔄 Ablauf

```
1. 🌐 Website abrufen
   ↓
2. 🔍 HTML-Element extrahieren
   ↓
3. 🧹 Daten bereinigen & formatieren
   ↓
4. 💾 In preis.json speichern
   ↓
5. ⏰ Zeitstempel setzen

```

---

**Haftungsausschluss (Disclaimer):**
Dieses Open-Source-Projekt wird kostenlos und „wie besehen“ (as is) ohne jegliche Gewährleistung, Garantie oder Zusage der Betriebsbereitschaft zur Verfügung gestellt. Jegliche Haftung für Schäden, die direkt oder indirekt aus der Nutzung der Daten oder des Scrapers entstehen (insbesondere durch fehlerhafte Preisauslesung oder Ausfälle), ist ausgeschlossen. Die Bereitstellung erfolgt freibleibend und nur bis auf Widerruf. Bei Beschwerden oder Einwänden wenden Sie sich bitte an: chrsbrmr@duck.com.
