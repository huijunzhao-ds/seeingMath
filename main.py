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
    Seeing the Examples is a website aiming at illustrating the math concepts and theories 
    using interactive examples. The website is under construction.  
    '''.replace('\n', ' ')
    
    st.sidebar.title("Seeing the Examples")
    st.sidebar.write(about)
    course, chapter, section = content_select()
    display_content(course, chapter, section)
    return 


if __name__ == '__main__':
    run_app()