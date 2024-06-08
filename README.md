`python -m venv .venv`
`.venv\Scripts\Activate`
`pip install streamlit`
`pip freeze > requirements.txt`
`streamlit run main.py`



## Projektbeschreibung
Dieses Projekt hat das Ziel, Personen in einem Dashboard anzuzeigen und EKG-Daten zu visualisieren. Das Dashboard ermöglicht es, Peaks in den EKG-Daten zu identifizieren und die Herzfrequenz zu berechnen.

## Installation und Ausführung

### Setup

1. Erstellen Sie eine virtuelle Umgebung:
    ```sh
    python -m venv .venv
    ```

2. Aktivieren Sie die virtuelle Umgebung:
    ```sh
    .venv\Scripts\Activate
    ```

3. Installieren Sie die benötigten Bibliotheken:
    zum Beispiel:
    ```sh
    pip install streamlit
    ```

4. Speichern Sie die installierten Bibliotheken in einer `requirements.txt` Datei:
    ```sh
    pip freeze > requirements.txt
    ```

5. Starten Sie die Streamlit-App:
    ```sh
    streamlit run main.py
    ```

## Projektstruktur

### Personen-Klasse (`person.py`)
Die Personen-Klasse repräsentiert eine Person und enthält Methoden zur Berechnung des Alters und der maximalen Herzfrequenz. Die Klasse kann Personen aus einer JSON-Datenbank laden.

Methoden der Person-Klasse:
`calc_age()`: Berechnet das Alter basierend auf dem Geburtsjahr.
`calc_max_heart_rate()`: Berechnet die maximale Herzfrequenz basierend auf dem Alter und Geschlecht.
`load_by_id()`: Instanziiert eine Person anhand der ID und der Datenbank.
`load_person_data()`: Lädt die Personendaten aus einer JSON-Datei (statische Methode).

### EKG-Test-Klasse (`ekgdata.py`)
Die Ekg-Test-Klasse repräsentiert einen EKG-Test und enthält Methoden zur Analyse und Visualisierung der EKG-Daten.

Methoden der EKG-Test-Klasse:
`load_by_id()`: Instanziiert einen EKG-Test anhand der ID und der Datenbank.
`find_peaks()`: Findet Peaks in den EKG-Daten und fügt diese als Attribut hinzu.
`estimate_hr()`: Berechnet die Herzfrequenz basierend auf den Peaks.
`plot_time_series()`: Erstellt einen Plot der EKG-Daten mit gefundenen Peaks.