# server.py
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq LLaMA model
model = ChatGroq(
    model="llama-3.1-8b-instant",  # exact model name
    groq_api_key=GROQ_API_KEY,
    temperature=0
)

# Prompt Template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Translate the following text into {language}:"),
    ("user", "{text}")
])

# Output parser
parser = StrOutputParser()

# Chain
chain = prompt_template | model | parser

# FastAPI app
app = FastAPI(
    title="LangChain Translator API",
    version="1.0",
    description="High-performance AI Translator using LangChain + Groq LLaMA 3.1"
)

# Add route to expose the chain
add_routes(app, chain, path="/translate")  # note the path: /translate

# Run server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
