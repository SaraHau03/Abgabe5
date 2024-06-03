import json
import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


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
        print(f"Peaks gefunden bei: {peaks}")
        return peaks
    
    def estimate_hr(self):
        # Calculate heart rate based on the peaks
        if find_peaks is not None:
            num_peaks = len(self.peaks)
            duration = self.df['Time in ms'].iloc[-1] - self.df['Time in ms'].iloc[0]
            heart_rate = (num_peaks / duration) * 60000  # Convert to beats per minute
            print(f"Heart Rate: {heart_rate} bpm")
        else:
            print("No peaks found. Heart rate cannot be calculated.")


    
    def plot_time_series(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['Time in ms'], self.df['EKG in mV'], color='blue')
        plt.scatter(self.df['Time in ms'][self.peaks], self.df['EKG in mV'][self.peaks], color='red', marker='x')
        plt.xlabel('Time in ms')
        plt.ylabel('EKG in mV')
        plt.title('EKG Time Series with Peaks')
        plt.show()
    

if __name__ == "__main__":
    print("Welcome to the EKG Data Analysis Tool!")
    

    # Load person data and populate all_ekg_data class variable
    with open("data/person_db.json") as file:
        person_data = json.load(file)
    
    for person in person_data:
        EKGdata.all_ekg_data.extend(person["ekg_tests"])

   
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
