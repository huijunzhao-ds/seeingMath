import streamlit as st
import numpy as np
import pandas as pd


class Coin:
    def __init__(self, prob_h:float):
        self.results = ['Head', 'Tail']
        self.probs = [prob_h, 1-prob_h]
        self.outcomes = []

    def flip(self):
        idx = int(np.random.random() < self.probs[0])
        self.outcomes.append(self.results[idx])
       
    def flip_1k(self):
        for _ in range(1000):
            self.flip()

    def clear(self):
        self.outcomes = []


paragraph1 = '''
Some tutorial goes here.
'''

def generate_plot_data():
    ## TODO
    return


def chance_events():
    st.write("Under construction")

    return 

