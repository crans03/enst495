import streamlit as st
from Home_🏠 import read_file

survey_path = 'survey_text.md'

st.set_page_config(page_title="Survey Results", page_icon='📋')

# title
st.title(read_file(survey_path, 2, 2))

# markdown 
st.markdown(read_file(survey_path, 6, 16))

