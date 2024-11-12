import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API"))
model = genai.GenerativeModel("gemini-1.5-flash")

students = genai.upload_file(
  path="desempenho_estudantes_enem.csv", display_name="Notas do ENEM"
)

response = model.generate_content(
  [
    students,
    "Crie um relatorio sobre o desempenho dos alunos no ENEM. Fale de tendências nos grupos de estudantes."
  ]
)

print(response.text)