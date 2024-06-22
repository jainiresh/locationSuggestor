import google.generativeai as genai

genai.configure(api_key="AIzaSyDLHYtS6M8SbgbaGr52K6CPt1Vbm4xvffw")

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def getResponseForPrompt(city, state, country, mood):
    print (f"Mood : {mood}")
    prompt = f"Iam currenlty in the area {city}, State: {state},Country: {country}."
    keyValuePrompt = "While populating make sure, you use a key value pair, like a python dict, where the key would be the place name, and the value will be 'How this place would console my current mood or requirement ?'"
    confirmationText = " Dont respond me with any other text than the output json that i asked for"
    filterText = f" Suggest me locations, Make sure that you send only the place names, and also in a json format inside a code snippet, {keyValuePrompt} also make sure it is not a nested json, and send all the files in a flat json."
    moodPrompt = f" Please use the main keyword as : 'I feel like : {mood}' when suggestion locations, the main keyword denotes the primary user's mood. The keyword is very important. "
    masterPrompt = prompt+moodPrompt+filterText+confirmationText
    response = model.generate_content(masterPrompt)
    print(response.text)
    return response.text


# response = getResponseForPrompt("Chennai","Tamil Nadu", "India", "wanna watch a movie")

# response = response.replace("```json","")
# response = response.replace("```","")
# response = eval(response)
# print(type(response))