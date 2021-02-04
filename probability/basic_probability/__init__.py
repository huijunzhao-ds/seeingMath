from .chance_events import chance_events
from .random_variables import random_variables
from .expectation import expectation
from .variance import variance
from .conditional_probability import conditional_probability
import streamlit as st


def basic_probability(section):    
    section2fcn = {
        'Chance Events': chance_events,
        'Random Variables': random_variables,
        'Expectation': lambda : st.write('Expectation section coming soon'),
        'Variance': lambda : st.write('Variance section coming soon'),
        'Conditional Probability': lambda : st.write('Conditional Probability section coming soon'),
    }
    return section2fcn[section]()