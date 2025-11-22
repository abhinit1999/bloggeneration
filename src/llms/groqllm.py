from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
class GroqLLM:
    def __init__(self):
        load_dotenv()
    def get_llm(self):
        try:
            os.environ["GROQ_API_KEY"] = self.groq_api_key = os.getenv("GROQ_API_KEY")
            llm = ChatGroq(model_name="openai/gpt-oss-20b",api_key=self.groq_api_key)
            return llm
        except Exception as e:
            raise ValueError("Error occured with exception: {e}")
        