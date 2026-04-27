# ⚡ ÖMAG Marktpreis Scraper

> Tägliche Aktualisierung des Strommarktpreises von der ÖMAG

## 📋 Überblick

Dieses Repository aktualisiert die Datei **`preis.json`** täglich mit dem aktuellsten bekannten Marktpreis für Strom von der [ÖMAG (Österreichische Energiebörse)](https://www.oem-ag.at/).

Der Scraper ruft automatisch die Marktpreisdaten ab und speichert diese in einem strukturierten JSON-Format für einfache Verarbeitung und Integration.

## 🎯 Funktionalität

- ✅ Automatisches Scraping der ÖMAG-Website
- ✅ Tägliche Aktualisierung des Marktpreises
- ✅ Strukturierte JSON-Speicherung mit Metadaten
- ✅ Zeitstempe für Nachverfolgung
- ✅ Preisangaben in EUR/kWh

## 📦 Struktur

### Input

- 🌐 **Quelle**: https://www.oem-ag.at/marktpreis/

### Output

- 💾 **Datei**: `preis.json`
- 📊 **Format**: JSON mit folgendem Inhalt:
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

### Manuelles Ausführen

```bash
python scrape.py
```

### Automatisierung

Die tägliche Ausführung erfolgt über **GitHub Actions** (`.github/workflows/scrape.yml`). Der Scraper läuft automatisch jeden Tag zur konfigurierten Zeit.

### Home Assistant Integration

Den folgenden Eintrag in configuration.yaml hinzufügen:

```json
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
So kann man das Ergebnis auch direkt in evcc als Einspeisevergütung abrufen:
**neue Einspeisevergütung -> benutzerdefiniertes Gerät**

```yaml
price: # current price
source: http
uri: chrsbrmr/oemag-marktpreis@refs/heads/main/preis.json (raw)
jq: .oemag_marktpreis
```

## 📦 Abhängigkeiten

- `requests` - HTTP-Requests
- `beautifulsoup4` - HTML-Parsing

## 🔄 Workflow

```
1. 🌐 Website abrufen
   ↓
2. 🔍 HTML-Element extrahieren
   ↓
3. 🧹 Daten bereinigen & formatieren
   ↓
4. 💾 In preis.json speichern
   ↓
5. ⏰ Mit Zeitstempel dokumentieren
```

## 📝 Lizenz

Dieses Projekt wird bereitgestellt "wie es ist" für persönliche und kommerzielle Nutzung.

---

**Zuletzt aktualisiert**: 29. März 2026 ✨
