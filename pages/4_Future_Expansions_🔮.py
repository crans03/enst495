import streamlit as st
from Home_🏠 import read_file

future_path = 'future_text.md'

st.set_page_config(page_title="Future Exploration", page_icon='🔮')

#title 
st.title(read_file(future_path, 2,2))

#paragraph
st.markdown(read_file(future_path, 6, 14))
