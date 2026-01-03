# 🌍 AI Translator (LangChain + Streamlit)

An **AI-powered multilingual translator** built using **LangChain**, **FastAPI**, and **Streamlit**.  
It automatically detects the source language and translates text into multiple target languages using an LLM backend.

---

## 🚀 Features

- 🌐 **Automatic Language Detection** (using `langdetect`)
- 🤖 **AI-based Translation** via LangChain backend
- 🖥️ **Interactive Streamlit UI**
- 📜 **Translation History** (session-based)
- 💾 **Download Translated Text**
- 🎯 Multiple target languages supported:
  - French
  - German
  - Spanish
  - Hindi
  - Japanese

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: FastAPI + LangChain  
- **LLM Provider**: Groq / LangChain-supported model  
- **Language Detection**: `langdetect`  
- **HTTP Client**: `requests`

---

## 📂 Project Structure

```text
AI-TRANSLATOR/
│
├── app.py              # Streamlit frontend
├── backend/            # FastAPI + LangChain backend
│   └── main.py
├── requirements.txt
└── README.md
