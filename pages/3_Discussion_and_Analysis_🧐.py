import streamlit as st
from Home_🏠 import read_file

discussion_path = 'discussion_text.md'

st.set_page_config(page_title="Discussion and Analysis", page_icon='🧐')

#title 
st.title(read_file(discussion_path, 2,2))

#heading 
st.header(read_file(discussion_path, 6,6))

#paragraph
st.markdown(read_file(discussion_path, 10, 18))
