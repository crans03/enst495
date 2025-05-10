import streamlit as st
from Home import read_file

interview_path = 'interview_text.md'

st.set_page_config(page_title="Interview Results", page_icon='🗣️')

#title
st.title(read_file(interview_path, 2,2))

#heading 
st.header(read_file(interview_path, 6,6))

#paragraph 
st.markdown(read_file(interview_path, 10, 19))

#heading
st.header(read_file(interview_path, 23, 23))

#paragraph
st.markdown(read_file(interview_path, 27, 29))

#heading ### UNIQUE ELEMENTS
st.header(read_file(interview_path, 33, 33))

#subheading #
st.subheader(read_file(interview_path, 37, 37))

#paragraph
st.markdown(read_file(interview_path, 41, 41))

#subheading #
st.subheader(read_file(interview_path, 45, 45))

#paragraph
st.markdown(read_file(interview_path, 49, 49))

#subheading #
st.subheader(read_file(interview_path, 53, 53))

#paragraph
st.markdown(read_file(interview_path, 57, 57))

#subheading #
st.subheader(read_file(interview_path, 61, 61))

#paragraph
st.markdown(read_file(interview_path, 65, 65))

#subheading #
st.subheader(read_file(interview_path, 69, 69))

#paragraph
st.markdown(read_file(interview_path, 73, 73))

#subheading #
st.subheader(read_file(interview_path, 77, 77))

#paragraph
st.markdown(read_file(interview_path, 81, 81))
