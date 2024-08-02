import streamlit as st
from transformers import pipeline
import time

# Load the classifier pipeline
classifier = pipeline("text-classification", model="jayavibhav/DistillBERT-Prompt-Injection-sm")

# Set the title and styling of the app
st.set_page_config(page_title="Prompt Evaluation", page_icon="🔍")
st.title("🔍 Prompt Evaluation")

# Sidebar for additional options or information
with st.sidebar:
    st.header("About")
    st.markdown("This app uses a pre-trained DistilBERT model to classify text into three categories: **SAFE**, **UNSAFE**, and **INJECTION**.")
    st.markdown("The classification is done in real-time and is visualized with color-coded labels.")

# Add custom CSS for styling and footer positioning
st.markdown("""
    <style>
        .stTextArea textarea {
            background-color: #f0f0f5;
            color: #000000;
            font-size: 16px;
            border-radius: 5px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 8px 16px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .stAlert div {
            font-size: 18px;
        }
        footer {
            font-size: 14px;
            text-align: center;
            padding: 10px;
            background-color: #f0f0f5;
            border-radius: 5px;
            margin-top: 20px;
            position: fixed;
            bottom: 0;
            width: 100%;
            left: 0;
        }
        .main {
            min-height: 90vh;
            padding-bottom: 60px; /* Space for the footer */
            box-sizing: border-box;
        }
    </style>
""", unsafe_allow_html=True)

# Container to wrap the main content
st.markdown("<div class='main'>", unsafe_allow_html=True)

# Text area for user input
st.markdown("### Enter the text to evaluate:")
user_input = st.text_area("", height=150, placeholder="Type your text here...")

# Submit button with a loading animation and progress bar
if st.button("Submit"):
    if user_input:
        with st.spinner('Evaluating...'):
            progress = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)  # Simulate a delay for the loading animation
                progress.progress(percent_complete + 1)

            result = classifier(user_input)
            label = result[0]['label']
            score = result[0]['score']

            # Display the result with color coding
            if label == 'SAFE':
                st.success(f"**{label}** with a confidence score of **{score:.3f}**")
            elif label == 'UNSAFE':
                st.warning(f"**{label}** with a confidence score of **{score:.3f}**")
            elif label == 'INJECTION':
                st.error(f"**{label}** with a confidence score of **{score:.3f}**")
    else:
        st.warning("Please enter some text before submitting.")

# Close the main container
st.markdown("</div>", unsafe_allow_html=True)

# Footer section
st.markdown("""
    <footer>
        © 2024 Prompt Evaluation App. All rights reserved.
    </footer>
""", unsafe_allow_html=True)
