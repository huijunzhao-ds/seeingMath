import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


rv_tutorial = '''
    A random variable is a function assigning a real number to each outcome in the probability
    space. 
'''
def random_variables():
    st.write(rv_tutorial)
    
    st.write('')
    return 