import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Smart Research Assistant", page_icon="📄", layout="wide")


def load_lottie_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)



st.title("Smart Assistant for Research Summarization")




uploaded_file = st.file_uploader("PDF file", type=["pdf", "txt"])

if uploaded_file:
   

    try:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:7860/upload/", files=files)

        if response.status_code != 200:
            st.error("Backend error.")
        else:
            result = response.json()

            if "error" in result:
                st.error("❌ " + result["error"])
            else:
                st.subheader("📋 Auto Summary")
                st.markdown(f"""
                <div style='background-color:#f0f2f6;padding:1.5rem;border-radius:10px;'>
                    {result['summary']}
                </div>
                """, unsafe_allow_html=True)

                mode = st.radio("Choose Mode:", ["Ask Anything", "Challenge Me"], horizontal=True)

                if mode == "Ask Anything":
                    question = st.text_input(" Ask your question:")
                    if question:
                        res = requests.post("http://127.0.0.1:7860/ask/", files=files, data={"question": question})
                        data = res.json()
                        if "error" in data:
                            st.error(+ data["error"])
                        else:
                            st.success("💬 Answer: " + data["answer"])
                            st.caption(+ data["justification"])

                elif mode == "Challenge Me":
                    res = requests.post("http://127.0.0.1:7860/challenge/", files=files)
                    data = res.json()
                    if "error" in data:
                        st.error(+ data["error"])
                    else:
                        st.subheader("🧠 Try answering:")
                        for i, q in enumerate(data["questions"]):
                            st.text_input(f"Q{i+1}: {q}", key=f"q{i}")

    except Exception as e:
        st.error(f"❌ Unexpected error: {e}")