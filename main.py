import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

groq_key = os.getenv("groq_api_key")
lang_smith_key= os.getenv("lang_smith_api_key")

os.environ["LANGCHAIN_API_KEY"] = lang_smith_key
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "CourseLanggraph"

llm = ChatGroq(groq_api_key=groq_key, model_name="llama-3.1-8b-instant")

response = llm.invoke("Best Asian food in Montreal?")
print(response.content)