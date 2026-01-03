
import requests
import streamlit as st
from langdetect import detect


API_URL = "http://127.0.0.1:8000/translate/invoke"

# -------------------- Backend Call --------------------
def get_groq_response(input_text, target_language="French"):
    payload = {
        "input": {
            "text": input_text,
            "language": target_language
        },
        "config": {},
        "kwargs": {
            "additionalProp1": {}
        }
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("output", "No output returned")
    else:
        return f"Error: {response.text}"

# -------------------- Streamlit UI --------------------
st.set_page_config(page_title="🌍 AI Translator", page_icon="🌐", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        padding: 8px 16px;
    }
    .stDownloadButton>button {
        background-color: #2196F3;
        color: white;
        border-radius: 8px;
        font-size: 14px;
        padding: 6px 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("⚙️ Options")
page = st.sidebar.radio("Navigate", ["🌍 Translator", "📜 History"])

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []
if "last_output" not in st.session_state:
    st.session_state.last_output = ""

# -------------------- Translator Page --------------------
if page == "🌍 Translator":
    st.title("🌍 AI Translator")
    st.markdown("Translate text instantly using **LangChain-powered AI** 🚀")

    input_text = st.text_area(
        "✍️ Enter text to translate",
        placeholder="Type your sentence here..."
    )

    if input_text.strip():
        detected_lang = detect(input_text)
        st.info(f"Detected source language: **{detected_lang}**")

    language = st.selectbox(
        "🎯 Select target language",
        ["French", "German", "Spanish", "Hindi", "Japanese"]
    )

    if st.button("Translate 🚀"):
        if input_text.strip():
            with st.spinner("Translating with AI..."):
                output = get_groq_response(input_text, language)
            st.success("✅ Translation completed!")
            st.write(output)

            # Save to history
            st.session_state.history.append((input_text, language, output))
            st.session_state.last_output = output
        else:
            st.warning("⚠️ Please enter some text")

    if st.session_state.last_output:
        st.download_button(
            label="💾 Download Translation",
            data=st.session_state.last_output,
            file_name="translation.txt",
            mime="text/plain"
        )

# -------------------- History Page --------------------
elif page == "📜 History":
    st.title("📜 Translation History")
    if st.session_state.history:
        for idx, (src, lang, out) in enumerate(st.session_state.history):
            st.write(f"{idx+1}. **{src}** → *{lang}*: {out}")
    else:
        st.info("No translations yet. Try the Translator tab!")

