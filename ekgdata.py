import json
import pandas as pd
import scipy.signal
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go


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

    

    def find_peaks(self, threshold,distance):
        series = self.df['EKG in mV']
        peaks, _ = scipy.signal.find_peaks(series, height=threshold,distance=distance)
        self.peaks = peaks
        return peaks
    
    def estimate_hr(self):
        if self.peaks is not None:
            num_peaks = len(self.peaks)
            duration = self.df['Time in ms'].iloc[-1] - self.df['Time in ms'].iloc[0]
            heart_rate = (num_peaks / duration) * 60000  # Convert to beats per minute
            print(f"Heart Rate: {heart_rate:.2f} bpm")
        else:
            print("No peaks found. Heart rate cannot be calculated.")
        self.heart_rate = heart_rate
        return heart_rate
    
    def plot_time_series(self):
        fig = go.Figure()
        
        # Add EKG time series data
        fig.add_trace(go.Scatter(x=self.df['Time in ms'], y=self.df['EKG in mV'],
                                 mode='lines', name='EKG in mV'))
        
        # Add peaks
        if self.peaks is not None:
            fig.add_trace(go.Scatter(x=self.df['Time in ms'].iloc[self.peaks], 
                                     y=self.df['EKG in mV'].iloc[self.peaks],
                                     mode='markers', name='Peaks',
                                     marker=dict(color='red', size=10, symbol='x')))
        
        fig.update_layout(title='EKG Time Series with Peaks',
                          xaxis_title='Time in ms',
                          yaxis_title='EKG in mV')
        
        return fig