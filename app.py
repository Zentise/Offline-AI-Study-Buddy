import streamlit as st
import requests

st.title("🧠 Offline AI Study Buddy (Mistral via Ollama)")

query = st.text_input("Ask me anything:")

if st.button("Get Answer"):
    if query:
        with st.spinner("Thinking..."):
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "mistral",
                    "prompt": query,
                    "stream": False
                }
            )
            result = response.json()["response"]
            st.success(result)
