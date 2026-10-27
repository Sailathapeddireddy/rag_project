import streamlit as st
import requests


st.title("Employee Handbook RAG Chatbot")

st.write("Ask questions about the Employee Handbook")


question = st.text_input("Enter your question")


if st.button("Ask"):

    if question:

        response = requests.post(
            "http://api:8000/ask",
            json={"question": question}
        )

        result = response.json()

        st.subheader("Answer")
        st.write(result["answer"])

    else:

        st.warning("Please enter a question.")