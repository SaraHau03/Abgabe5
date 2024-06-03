import streamlit as st
from ekgdata import EKGdata
from person import Person

def main():
    st.title("EKG Data Analysis Tool")

    # Load person data and populate all_ekg_data class variable
    person_data = Person.load_person_data()
    for person in person_data:
        EKGdata.all_ekg_data.extend(person["ekg_tests"])

    person_names = Person.get_person_list(person_data)
    selected_person_name = st.selectbox("Wählen Sie eine Person", ["Auswählen"] + person_names)
    if selected_person_name != "Auswählen":
        person_dict = Person.find_person_data_by_name(selected_person_name)
        if person_dict:
            st.write(f"Name: {person_dict['firstname']} {person_dict['lastname']}")
            st.write(f"Geburtsdatum: {person_dict['date_of_birth']}")
            st.image(person_dict['picture_path'])

            selected_ekg_id = st.selectbox("Wählen Sie eine EKG-ID", [ekg["id"] for ekg in person_dict["ekg_tests"]])
            if selected_ekg_id:
                ekg_by_id = EKGdata.load_by_id(selected_ekg_id)
                if ekg_by_id:
                    st.write("Die Herzfrequenz lautet:")
                    ekg_by_id.find_peaks(threshold=320, distance=150)
                    st.write(ekg_by_id.estimate_hr())
                    st.plotly_chart(ekg_by_id.plot_time_series())
                else:
                    st.write("Keine EKG-Daten mit der gegebenen ID gefunden.")
        else:
            st.write("Keine Person mit diesem Namen gefunden.")

if __name__ == "__main__":
    main()
