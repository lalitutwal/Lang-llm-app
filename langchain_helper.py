import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7
    )

    prompt = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
    )

    # This is the modern "Chain" using the pipe operator |
    # The previous one has been deprecated
    chain = prompt | llm | StrOutputParser()
    
    # Invoke the chain
    response = chain.invoke({'animal_type': animal_type, 'pet_color': pet_color})
    
    # Return in the format your Streamlit app expects
    return {'pet_name': response}