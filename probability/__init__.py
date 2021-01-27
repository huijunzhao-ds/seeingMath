from .basic_probability import basic_probability
import streamlit as st

def probability(chapter, section):
    chapter2fcn = {
        'Basic Probability': lambda section: basic_probability(section),
        'Distributions': lambda section: st.write("Distribution Chapter Coming soon"),
        'Frequentist Inference': lambda section: st.write("Frequentist Inference Chapter Coming soon"),
        'Bayesian Inference': lambda section: st.write("Bayesian Inference Chapter Coming soon"),
        'Regression Analysis': lambda section: st.write("Regression Analysis Chapter Coming soon"),
    }

    return chapter2fcn[chapter](section)
