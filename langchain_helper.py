from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key, temperature=0.5)

def get_restaurant_name_and_items(cuisine):
    
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest only one fancy name for this. Do not provide an explanation."
    )
    name_chain = prompt_template_name | llm
    
    restaurant_name = name_chain.invoke({"cuisine": cuisine}).strip()
    
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest 10 menu food items for {restaurant_name}. Seperate each menu item from each other with a comma and do not provide descriptions of the menu items."
    )
    items_chain = prompt_template_items | llm
    
    menu_items = items_chain.invoke({"restaurant_name": restaurant_name}).strip()
    
    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }
