import streamlit as st
from read_data import get_person_data, get_person_names, find_person_data_by_name
from PIL import Image


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


