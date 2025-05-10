import streamlit as st

def read_file(file_path, start_num, end_num):
    file = open(file_path, 'r')
    skippedContent = ""
    content = ""
    if start_num > 0:
        for x in range(start_num-1):
            skippedContent += file.readline()
    for x in range(start_num, end_num+1):
        content += file.readline()
    return content

references_path = 'references_text.md'

st.set_page_config(page_title="References", page_icon='📖')

# title 
st.title(read_file(references_path, 2, 2))

#paragraph
st.markdown(read_file(references_path, 6, 37))
