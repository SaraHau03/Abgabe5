import json
import pandas as pd
from scipy.signal import find_peaks

class EKGdata:
    # Class variable to hold all EKG data
    all_ekg_data = []

    def __init__(self, ekg_dict):
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['EKG in mV', 'Time in ms'])

    @staticmethod
    def find_ekg_data_by_id(ekg_id):
        """A Function that takes an ID and returns the EKG data as a dictionary"""
        for ekg_dict in EKGdata.all_ekg_data:
            if ekg_dict["id"] == ekg_id:
                return ekg_dict
        return None

    @classmethod
    def load_by_id(self,ekg_id_input):
        ekg_dict = self.find_ekg_data_by_id(ekg_id_input)
        if ekg_dict:
            return self(ekg_dict)
        else:
            return None

    def display(self):
        print(f"ID: {self.id}")
        print(f"Date: {self.date}")
        print(f"Data File: {self.data}")
        print(f"EKG Data (first 5 rows):\n{self.df.head()}")

    def find_peaks(self):
        # Find peaks in the EKG data
        peaks, _ = find_peaks(self.df['EKG in mV'], height=0)
        self.peaks = peaks
        print(f"Peaks found: {peaks}")

if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    

    # Load person data and populate all_ekg_data class variable
    with open("data/person_db.json") as file:
        person_data = json.load(file)
    
    for person in person_data:
        EKGdata.all_ekg_data.extend(person["ekg_tests"])

    # Example usage
    ekg_dict = person_data[0]["ekg_tests"][0]
    print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    print(ekg.df.head())
   
    try:
        ekg_id_input = int(input("Bitte geben Sie die ID der Person ein: "))
        ekg_by_id = EKGdata.load_by_id(ekg_id_input)
        if ekg_by_id:
            print("EKG Data loaded by ID:")
            ekg_by_id.display()
            ekg_by_id.find_peaks()
        else:
            print("Keine EKG-Daten mit der gegebenen ID gefunden.")
    except ValueError:
        print("Bitte geben Sie eine gültige numerische ID ein.")
