import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/study"  # FIXED

st.title("AI Agent Analyzer")

user_id = st.text_input("Enter user_id")
question = st.text_area("Enter text to get answer", height=200)

if st.button("Submit"):
    if not question.strip():
        st.warning("Please enter some text.")
    else:
        try:
            response = requests.post(
                API_URL,
                json={
                    "user_id": user_id.strip() or "default_user",
                    "question": question.strip()
                },
                timeout=120
            )

            if response.status_code == 200:
                data = response.json()
                st.subheader("Answer")
                st.write(data.get("response", "No response returned"))
            else:
                st.error("API Error")
                st.code(response.text)

        except requests.exceptions.ConnectionError:
            st.error("❌ Cannot connect to backend. Is FastAPI running?")

        except Exception as e:
            st.error(f"Error: {str(e)}")