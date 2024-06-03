import streamlit as st
from read_data import get_person_data, get_person_names, find_person_data_by_name
from PIL import Image
from person import Person
from ekgdata import EKGdata
import json

# Funktionen zum Laden und Anzeigen der Personendaten
def display_person_info(person_name):
    person_dict = find_person_data_by_name(person_name)
    image = Image.open(person_dict["picture_path"])
    st.image(image, caption=person_name)
    st.write("Es wurde folgender Nutzer gewählt: " + person_name)

# Funktionen zum Laden und Anzeigen der EKG-Daten
def display_ekg_data(ekg_id):
    ekg_data = EKGdata.load_by_id(ekg_id)
    if ekg_data:
        st.write("EKG Data loaded by ID:")
        ekg_data.display()
        ekg_data.find_peaks()
        ekg_data.estimate_hr()
        ekg_data.plot_time_series()
    else:
        st.write("Keine EKG-Daten mit der gegebenen ID gefunden.")

# Hauptfunktion der Streamlit-App
def main():
    # Laden der Personendaten
    person_data = get_person_data()
    person_names_list = get_person_names(person_data)

    # Session State wird leer angelegt, solange er noch nicht existiert
    if 'current_user' not in st.session_state:
        st.session_state.current_user = 'None'
    if 'ekg_ids' not in st.session_state:
        st.session_state.ekg_ids = []

    # Überschriften
    st.write("# EKG APP")
    st.write("## Versuchsperson auswählen")

    # Auswahlbox für Versuchsperson
    st.session_state.current_user = st.selectbox(
        'Versuchsperson',
        options=person_names_list, key="sbVersuchsperson")

    # Anzeigen der ausgewählten Personendaten
    if st.session_state.current_user != 'None':
        display_person_info(st.session_state.current_user)
        
        # Finden der Personendaten und Anzeigen der EKG-IDs
        person_dict = find_person_data_by_name(st.session_state.current_user)
        st.session_state.ekg_ids = [ekg["id"] for ekg in person_dict["ekg_tests"]]
        
        # Auswahlbox für EKG-IDs
        ekg_id = st.selectbox(
            'EKG ID auswählen',
            options=st.session_state.ekg_ids, key="sbEkgId")
        
        # Button zum Laden der EKG-Daten
        if st.button("EKG-Daten anzeigen"):
            display_ekg_data(ekg_id)

# Ausführung der Hauptfunktion
if __name__ == "__main__":
    main()
