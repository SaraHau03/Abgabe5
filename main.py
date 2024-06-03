import streamlit as st
from read_data import get_person_data, get_person_names, find_person_data_by_name
from PIL import Image
from person import Person
from ekgdata import EKGdata
import json
import streamlit as st
from read_data import get_person_data, get_person_names, find_person_data_by_name
from PIL import Image
from person import Person
from ekgdata import EKGdata
import json



person_data = get_person_data()
person_names_list = get_person_names(person_data)

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

# Eine Überschrift der ersten Ebene
st.write("# EKG APP")

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Eine Auswahlbox, das Ergebnis wird in current_user gespeichert
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_names_list, key="sbVersuchsperson")

# Laden eines Bilds
person_dict = find_person_data_by_name(st.session_state.current_user)

image = Image.open(person_dict["picture_path"])
# Anzeigen eines Bilds mit Caption

st.image(image, caption=st.session_state.current_user)

st.write("Es wurde folgender Nutzer gewählt: " + st.session_state.current_user)



if __name__ == "__main__":
    print("This is a module with some functions to read the person data")
    persons = Person.load_person_data()
    person_names = Person.get_person_list(persons)
    print(person_names)
    print(Person.find_person_data_by_name("Heyer, Yannic"))
    selected_person = Person(Person.find_person_data_by_name("Heyer, Yannic"))
    print(selected_person.calc_max_heart_rate())
     # Load person data and populate all_ekg_data class variable
    with open("data/person_db.json") as file:
        person_data = json.load(file)
    
    for person in person_data:
        EKGdata.all_ekg_data.extend(person["ekg_tests"])

    try:
        person_id_input = int(input("Bitte geben Sie die ID der Person ein: "))
        person_by_id = Person.load_by_id(person_id_input)
        if person_by_id:
            print(f"Person loaded by ID: {person_by_id.firstname} {person_by_id.lastname}")
            print(f"Das Alter beträgt:",person_by_id.calc_age())
            print(f"Max Herzfrequenz: {person_by_id.calc_max_heart_rate()} bpm")
        else:
            print("Keine Person mit der gegebenen ID gefunden.")
    except ValueError:
        print("Bitte geben Sie eine gültige numerische ID ein.")
   
    try:
        ekg_id_input = int(input("Bitte geben Sie die ID der Person ein: "))
        ekg_by_id = EKGdata.load_by_id(ekg_id_input)
        if ekg_by_id:
            print("EKG Data loaded by ID:")
            ekg_by_id.display()
            ekg_by_id.find_peaks()
            ekg_by_id.estimate_hr()
            ekg_by_id.plot_time_series()
        else:
            print("Keine EKG-Daten mit der gegebenen ID gefunden.")
    except ValueError:
        print("Bitte geben Sie eine gültige numerische ID ein.")


