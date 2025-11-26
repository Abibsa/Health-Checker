"""
Test script untuk mencari model Gemini yang tersedia
"""
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    print("ERROR: GEMINI_API_KEY not found!")
    exit(1)

print(f"API Key: {api_key[:10]}...")

genai.configure(api_key=api_key)

print("\nListing available models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"- {model.name}")
        print(f"  Display name: {model.display_name}")
        print(f"  Description: {model.description[:100]}...")
        print()
