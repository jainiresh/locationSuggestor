import google.generativeai as genai
import PIL.Image
import os

genai.configure(api_key="AIzaSyDLHYtS6M8SbgbaGr52K6CPt1Vbm4xvffw")
img = PIL.Image.open('./services/test.png')

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def getResponseForPrompt(mood, city, state, country):
    prompt = f"Im {mood}, and im in {city}, {state}, {country}."
    confirmationText = " Dont respond me with any other text than the output json that i asked for"
    filterText = " Suggest me locations, Make sure that you send only the place names, and also in a json format inside a code snippet, use the format : data: <populate Here>, also make sure it is not a nested json, and send all the files in a flat json."
    response = model.generate_content(prompt+filterText+confirmationText)
    print(response.text)
    return response.text
