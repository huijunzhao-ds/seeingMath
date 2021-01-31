import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


class Coin:
    def __init__(self, prob_h:float):
        self.results = ['Head', 'Tail']
        self.imgs = [Image.open('probability/images/head.png'),
                    Image.open('probability/images/tail.png')]
        self.probs = [prob_h, 1-prob_h]
        self.outcomes = []  


    def flip(self):
        self.outcomes.append(int(np.random.random() > self.probs[0]))


    def flip_n(self, n:int):
        for _ in range(n):
            self.flip()


    def generate_plot_data(self):
        return pd.DataFrame({'Head':[len(self.outcomes) * self.probs[0],
                                     len(self.outcomes) - sum(self.outcomes)], 
                             'Tail': [len(self.outcomes) * self.probs[1], 
                                      sum(self.outcomes)]}, 
                             index=['Simulation', 'Truth'])



coin_tutorial = '''
    *Probability Theory* is the math formalization of *randomness*. We introduce 
    the classic coin toss simulation below as our first random experiment.

    The two possible outcomes, or __events__ in Probability Theory, are Head and Tail.
    The __probability__ of an event is a number between 0 and 1 indicating how likely 
    the event will happen, where 0 indicates impossibility and 1 indicates certainty. 
    For a *fair* coin, the probability of Head is 0.5, equaling to that of Tail. For an
    *unfair* or *weighted* coin, you can set the probability of Head in the slider bar below.

    Flipping the coin for multiple times, we may get more or less Heads than the true probability.
    But as the number of flips increases, the long-run frequency gets closer and closer to, or 
    equivalently __converges to__ the true probabilty, as shown in the histogram on the right below. 
'''

def coin_simulate():
    left_column, right_column = st.beta_columns(2)
    left_column.empty()
    right_column.empty()
    
    p = left_column.slider('True probability for Head', 
                           min_value=0.0, max_value=1.0, value=0.5)
    coin = Coin(p)

    n = left_column.number_input('Flip the coin for following times', min_value=0)
    if n > 0:
        coin.flip_n(n)
        left_column.image(coin.imgs[coin.outcomes[-1]], width=200)
        hist_data = coin.generate_plot_data()
        right_column.bar_chart(hist_data, 
                               height=400,
                               use_container_width=True)
    else:
        left_column.image(Image.open('probability/images/head.png'), width=200)
        right_column.bar_chart(pd.Series({'Head':0, 'Tail':0}), 
                               height=400,
                               use_container_width=True)


def chance_events():
    st.write(coin_tutorial)
    coin_simulate()
    return 