import streamlit as st
from transformers import pipeline
import time

# Load the classifier pipeline
classifier = pipeline("text-classification", model="jayavibhav/DistillBERT-Prompt-Injection-sm")

# Set the title and styling of the app
st.set_page_config(page_title="Prompt Evaluation", page_icon="🔍")
st.title("🔍 Prompt Evaluation")

# Add a description or instructions
st.markdown("Enter text in the box below to evaluate its safety. The app will classify the text into one of three categories: **SAFE**, **UNSAFE**, or **INJECTION**.")

# Add custom CSS for styling
st.markdown("""
    <style>
        .stTextArea textarea {
            background-color: #f0f0f5;
            color: #000000;
            font-size: 16px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
        }
        .stProgress div {
            background-color: #4CAF50;
        }
    </style>
""", unsafe_allow_html=True)

# Text area for user input
user_input = st.text_area("Enter the text to evaluate:")

# Submit button with a loading bar
if st.button("Submit"):
    with st.spinner('Evaluating...'):
        time.sleep(1)  # Simulate a delay for the loading animation
        result = classifier(user_input)
        label = result[0]['label']
        score = result[0]['score']

        # Display the result with color coding
        if label == 'SAFE':
            st.success(f"The text is classified as **{label}** with a confidence score of **{score:.2f}**")
        elif label == 'UNSAFE':
            st.warning(f"The text is classified as **{label}** with a confidence score of **{score:.2f}**")
        elif label == 'INJECTION':
            st.error(f"The text is classified as **{label}** with a confidence score of **{score:.2f}**")
