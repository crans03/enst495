import streamlit as st

home_path = 'home_text.md'

st.set_page_config(page_title="Hello", page_icon='🏠')

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

#title
st.title(read_file(home_path, 2,2))

#heading
st.header(read_file(home_path, 6,6))

#paragraph
st.markdown(read_file(home_path, 10,10))

#heading
st.header(read_file(home_path, 14,14))

#paragraph
st.markdown(read_file(home_path, 18,20))

#subheading
st.subheader(read_file(home_path, 24,24))

#paragraph
st.markdown(read_file(home_path, 28,30))

#image, caption
st.image('suay_.png', caption=read_file(home_path,37,37))

#subheading
st.subheader(read_file(home_path, 41,41))

#paragraph
st.markdown(read_file(home_path, 45,53))

#heading
st.header(read_file(home_path, 57, 57))

#paragraph
st.markdown(read_file(home_path, 61,63))

#heading 
st.header(read_file(home_path, 67, 67))

#paragraph
st.markdown(read_file(home_path, 71,75))

#heading 
st.header(read_file(home_path, 79, 79))

#paragraph
st.markdown(read_file(home_path, 83,83))
