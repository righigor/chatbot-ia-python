import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API"))

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Crie uma historia sobre um cachorro que adora brincar com seu dono.")
print(response.text)