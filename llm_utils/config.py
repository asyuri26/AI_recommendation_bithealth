import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

# Muat isi .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Ambil API key dari environment
openai_api_key = os.getenv("OPENAI_API_KEY")

# Inisialisasi model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    max_tokens=20,
    openai_api_key=openai_api_key
)