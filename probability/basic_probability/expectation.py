import streamlit as st
import pandas as pd
class Dice:
    def __init__(self, probs):
        self.results = ['Head', 'Tail']
        ## TODO find images
        self.imgs = [Image.open('probability/images/head.png'),
                    Image.open('probability/images/tail.png')]
        self.probs = probs
        self.outcomes = []  


    def roll(self):
        p = np.random.random()
        for res, tp in enumerate(self.probs):
            if p > tp:
                p -= tp
            else:
                self.outcomes.append(res)
                return


    def roll_n(self, n:int):
        for _ in range(n):
            self.roll()


    def generate_plot_data(self):
        ## TODO
        return pd.DataFrame({'Truth':[len(self.outcomes) * p for p in self.probs], 
                             'Simulation': [len(self.outcomes) - sum(self.outcomes), 
                                            sum(self.outcomes)]}, 
                             index=[1, 2, 3, 4, 5, 6]).T

def expectation():
    st.write("Coming Soon")
    return 