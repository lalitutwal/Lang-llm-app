import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate



load_dotenv()
# Ensure your GROQ_API_KEY environment variable is set
# Or pass it directly: llm = ChatGroq(api_key="your_key", model="llama-3.3-70b-versatile")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

#

#langchain.chain

messages = [
    ("system", "You are a helpful assistant."),
    ( "How fast is Groq's inference?"),
]

response = llm.invoke(messages)
print(response.content)
