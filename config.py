import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

print("API KEY:", os.getenv("OPENROUTER_API_KEY"))
print("MODEL:", os.getenv("MODEL_NAME"))
def get_llm():
    """
    Returns configured LLM using OpenRouter
    """
    return ChatOpenAI(
    openai_api_key=os.environ.get("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model=os.environ.get("MODEL_NAME"),
    temperature=0.7
    )
llm = get_llm()

print(llm.invoke("Hello world"))