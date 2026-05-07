import os
from dotenv import load_dotenv

load_dotenv()

groq_key = os.getenv("groq_api_key")
lang_smith_key= os.getenv("lang_smith_api_key")


print(lang_smith_key)