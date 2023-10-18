
import streamlit as st
import json
import os

# Load the cybersecurity concepts from the JSON file
with open(os.path.join(os.path.dirname(__file__), 'InfoSecConcepts.json'), 'r') as file:
    concepts = json.load(file)

# Extract titles for the autocomplete search box
titles = [concept["Title"] for concept in concepts]

# Streamlit UI
st.title("CyberSecurity Concepts")
st.markdown(
    """
    Shout out to [Brandon Chiles](https://www.linkedin.com/in/brandon-chiles/) for sharing this resource in our cohort. This tool allows you search for different concepts and guides you on what to study.
"""
)
selected_title = st.selectbox("Search for a concept:", titles, index=None,  format_func=lambda x: x)

# Display the information for the selected concept
for concept in concepts:
    if concept["Title"] == selected_title:
        st.subheader("Questions")
        for question in concept["Questions"]:
            st.write("- " + question)

        st.subheader("Objectives")
        for objective in concept["Objectives"]:
            st.write("- " + objective)

        st.subheader("Vocabulary")
        for word in concept["Vocabulary"]:
            st.write("- " + word)
