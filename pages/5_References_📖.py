import streamlit as st
from Home import read_file

references_path = 'references_text.md'

st.set_page_config(page_title="References", page_icon='📖')

#paragraph
st.markdown(read_file(references_path, 2, 28))
