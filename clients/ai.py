from django.conf import settings
from google import genai

#read the api key from django setting
api_key = settings.GEMINI_API_KEY

#Create the gemini client only when a key is configured
gemini_client = genai.Client(api_key=api_key) if api_key else None

#sending the question to gemini
def ask_gemini(question):
    #stop early if the api key has not been configured
    if gemini_client is None: 
        raise ValueError("The Gemini api key is missing")
    
    #if it is conigured we send research question to gemini api
    response = gemini_client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=question
    )

    #return the ai generated response text
    return response.text