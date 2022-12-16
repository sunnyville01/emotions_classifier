import streamlit as st
from model import GeneralModel


def app():

    # Creating an object of prediction service
    pred = GeneralModel()

    api_key = st.sidebar.text_input("APIkey", type="password")
    # Using the streamlit cache
    @st.cache
    def process_prompt(input):

        return pred.model_prediction(input=input.strip(), api_key=api_key)

    if api_key:

        # Setting up the Title
        st.title("Emotions Classification")

        st.markdown(
            """This app uses the GPT-3 Model that has been finetuned on the [Emotions Dataset](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp) to classify text between the following emotions: sadness, anger, love, surprise, fear and joy"""
        )
        # st.write("---")
        input = st.text_area(
            label="Enter Text",
            max_chars=150,
            height=100,
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")
