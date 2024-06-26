import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
