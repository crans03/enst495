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

survey_path = 'survey_text.md'

st.set_page_config(page_title="Survey Results", page_icon='📋')

# title
st.title(read_file(survey_path, 2, 2))

# markdown 
st.markdown(read_file(survey_path, 6, 16))

