import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API"))
model = genai.GenerativeModel("gemini-1.5-flash")

with open("curriculo.txt", "r") as file:
    text = file.read()

response = model.generate_content(f"Pode, por favor, avaliar o seguinte curriculo? {text}")

print(response.text)