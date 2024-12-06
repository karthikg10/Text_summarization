import streamlit as st
from transformers import pipeline

# Load model from Hugging Face
@st.cache_resource
def load_model():
    summarizer = pipeline("summarization", model="karthikganesh/report_model")
    return summarizer

summarizer = load_model()

# Streamlit UI setup
st.title("Text Summarization App")
st.write("Enter a paragraph, and the model will summarize it for you!")

# User input
user_input = st.text_area("Input Text", "Paste your text here...")

if st.button("Summarize"):
    if user_input.strip():
        with st.spinner("Generating summary..."):
            summary = summarizer(user_input, max_length=150, min_length=30, do_sample=False)
            st.subheader("Summary:")
            st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
