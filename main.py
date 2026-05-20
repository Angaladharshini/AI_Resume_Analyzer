import streamlit as st
import pdfplumber
import re


skills_list = [
    "python", "java", "c", "sql", "html",
    "css", "javascript", "machine learning",
    "communication", "excel"
]


def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text.lower()


def find_skills(text):
    found = []
    for skill in skills_list:
        if skill in text:
            found.append(skill)
    return found


st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

if uploaded_file:
    resume_text = extract_text(uploaded_file)

    skills = find_skills(resume_text)

    st.subheader("Detected Skills")
    st.write(skills)

    score = len(skills) * 10
    st.subheader("Resume Score")
    st.write(score, "/100")

    if "python" in skills and "sql" in skills:
        st.success("Suggested Role: Data Analyst")
    elif "html" in skills and "css" in skills:
        st.success("Suggested Role: Web Developer")
    else:
        st.warning("Add more skills to improve resume")