import google.generativeai as genai

def init_gemini(api_key: str):
    genai.configure(api_key=api_key)

def get_gemini_model():
    return genai.GenerativeModel("gemini-2.5-flash")
