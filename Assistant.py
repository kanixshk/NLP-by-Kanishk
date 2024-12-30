import speech_recognition as sr
import torch
import pyttsx3
import datetime

if __name__ == "__main__":
    model_name = input("Please enter your model name: ")
    print(f"Initializing {model_name}...")
    
    
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning....")
    elif hour>=12 and hour<=18:
        speak("Good afternoon....")
    else:
        speak("Good Evening....")
    speak("I am your virtual assistant sir, please tell me how can i help you")

def listen_to_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None
        
def verify_input(user_input):
    speak(f"Did you say '{user_input}'? (yes/no): ")
    print(f"Did you say '{user_input}'? (yes/no): ")
    confirmation = input()  # Capture user input directly
    return confirmation.lower() == 'yes'

import openai
import requests

openai.api_key = 'YOUR_API_KEY_HERE'
def query_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def google_search(query):
    api_key = 'YOUR_API_KEY_HERE'
    search_engine_id = 'YOUR_ENGINE_ID_HERE'
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}"
    
    response = requests.get(url)
    results = response.json()
    
    if 'items' in results:
        return results['items'][0]['snippet']  # Return the snippet of the first result
    else:
        return "No results found."

from transformers import AutoTokenizer, AutoModelForCausalLM
def define_and_use_tokenizer(model_name, text):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokens = tokenizer(text)
    define_and_use_tokenizer(model_name)


def generate_response(prompt):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=150, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response


def main():
    print("Welcome to your voice-activated virtual assistant!")
    
    while True:
        user_input = listen_to_voice()
        if user_input is None:
            continue
        
        if verify_input(user_input):
            
            #For open ai
            openai_response = query_openai(user_input)
            print(f"OpenAI Response: {openai_response}")

            #For google searches
            google_response = google_search(user_input)
            print(f"Google Search Result: {google_response}")
            
            # Generate response using LLaMA
            llama_response = generate_response(user_input)
            print(f"LLaMA Response: {llama_response}")
        else:
            print("Let's try again.")

if __name__ == "__main__":
    main()
