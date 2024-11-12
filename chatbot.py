import google.generativeai as genai
import os
import gradio

genai.configure(api_key=os.environ.get("GEMINI_API"))
model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat()

def gradio_wrapper(message, _history):
  text = message["text"]
  uploaded_files = []
  for files_info in message["files"]:
    file_path = files_info["path"]
    uploaded_file = genai.upload_file(file_path)
    uploaded_files.append(uploaded_file)
  response = chat.send_message(message)
  return response.text

chatInterface = gradio.ChatInterface(fn=gradio_wrapper, multimodal=True)
chatInterface.launch()