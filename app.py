import streamlit as st
from transformers import pipeline

# Load the classifier pipeline
classifier = pipeline("text-classification", model="jayavibhav/DistillBERT-Prompt-Injection-sm")

# Set the title of the app
st.title("Prompt Evaluation")

# Text area for user input
user_input = st.text_area("Enter the text to evaluate:")

# Submit button
if st.button("Submit"):
    with st.spinner('Evaluating...'):
        # Perform classification
        result = classifier(user_input)
        label = result[0]['label']
        score = result[0]['score']

        # Display the result
        if label == 'SAFE':
            st.success(f"The text is classified as {label} with a confidence score of {score:.2f}")
        else:
            st.error(f"The text is classified as {label} with a confidence score of {score:.2f}")
