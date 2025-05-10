import streamlit as st
from Home import read_file

process_path = 'process_text.md'

st.set_page_config(page_title="Survey and Interview Process", page_icon='⚙️')

# title
st.title(read_file(process_path, 2, 2))

# paragraph
st.markdown(read_file(process_path, 6, 6))

# heading
st.header(read_file(process_path, 10, 10))

# paragraph
st.markdown(read_file(process_path, 14, 64))

# heading
st.header(read_file(process_path, 68, 68))

# paragraph
st.markdown(read_file(process_path, 72, 86))
