import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import re

st.title("Question Paper Generator")

uploaded_file = st.file_uploader("Upload Syllabus PDF", type=["pdf"])

if uploaded_file is not None:
    # Extract text
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    st.write("Extracted syllabus preview:")
    st.write(text[:1000])

    # Your existing topic extraction and question paper generation logic here
    # ...

    if st.button("Generate Question Paper"):
        # Call your question paper creation function
        # Save document, etc.
        st.success("Question paper generated!")

