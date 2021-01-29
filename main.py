import streamlit as st
import time 
from content import CONTENT
from probability import probability

def content_select(content=CONTENT):
    course = st.sidebar.selectbox('Course', list(content.keys()))
    chapter = st.sidebar.selectbox('Chapter', list(content[course].keys()))
    section = st.sidebar.selectbox('Section', content[course][chapter])
    return course, chapter, section


def display_content(course, chapter, section):
    course2fcn = {
        'Probability': lambda chapter, section: probability(chapter, section),

    }

    return course2fcn[course](chapter, section)


def run_app():
    about = '''
    Seeing Math aims at illustrating the math concepts and theories 
    using interactive visualization. The website is still under construction.  
    '''
    
    contributors = '''
        #### Contributors
        - Huijun Zhao
    '''
    st.sidebar.title("Seeing Math")
    st.sidebar.write(about)
    course, chapter, section = content_select()
    display_content(course, chapter, section)

    st.sidebar.write(contributors)
    return 


if __name__ == '__main__':
    run_app()