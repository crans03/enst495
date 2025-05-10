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
