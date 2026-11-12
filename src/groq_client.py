import os
from groq import Groq 
from dotenv import load_dotenv
from src.tool_definitions import TOOLS

#Load environment variables from dotenv
load_dotenv()

#Retrieve the API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing from .env"
    )

#Initialize groq client
client = Groq(api_key=api_key)

#Model configuration
MODEL = "openai/gpt-oss-20b"

def get_response(messages, tools=None):
    
    #Sends conversation messages to groq and returns the LLM-generated response

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        temperature=0.7,
        max_completion_tokens=1000
    )

    return response.choices[0].message