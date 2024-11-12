import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API"))
model = genai.GenerativeModel("gemini-1.5-flash")

dog_1 = genai.upload_file(path="cachorro_golden_retriever.png")
dog_2 = genai.upload_file(path="cachorro_collie_acho.png")

response = model.generate_content(
  [
    dog_1,
    "Descubra a raça do cachorro na imagem. E me diga algumas curiosidades sobre a raça."
  ]
)

response2 = model.generate_content(
  [
    dog_2,
    "Descubra a raça do cachorro na imagem. E me diga algumas curiosidades sobre a raça."
  ]
)

print(response.text)
print(response2.text)