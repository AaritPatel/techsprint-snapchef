import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load the environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Configure the AI Model
if api_key:
    genai.configure(api_key=api_key)
else:
    raise ValueError("API Key not found in .env file")

def get_recipe(image_parts):
    """
    Sends the image to Google Gemini and asks for a recipe.
    """
    
    # 3. The Prompt (The Instructions for the AI)
    system_prompt = """
    You are an expert Chef called 'SnapChef'.
    Look at the ingredients in the image.
    1. Identify the ingredients you see.
    2. Suggest ONE delicious recipe I can make with these.
    3. You can assume I have basic pantry items (salt, pepper, oil, water).
    
    Format your response exactly like this:
    ## 🍽️ [Recipe Name]
    **⏱️ Cooking Time:** [Time]
    **💪 Difficulty:** [Easy/Medium/Hard]
    
    ### 🛒 Ingredients Found:
    * [List item 1]
    * [List item 2]
    
    ### 👩‍🍳 Instructions:
    1. [Step 1]
    2. [Step 2]
    3. [Step 3]
    
    If the image is not food, strictly say: "I don't see any food here! Please upload a photo of ingredients."
    """

    # 4. Select the Model (Gemini 1.5 Flash is fast and free)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # 5. Generate the Content
    response = model.generate_content([system_prompt, image_parts[0]])
    
    return response.text