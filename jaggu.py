import speech_recognition as sr
import torch
import pyttsx3
import datetime
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig
import webbrowser
import subprocess

# Define the model name
model_name = "C:\\codes\\llama1B\\" 

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning....")
    elif hour < 18:
        speak("Good afternoon....")
    else:
        speak("Good evening....")
    speak("I am your virtual assistant Jaggu, please tell me how can I help you.")

def listen_to_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Recognizing....")
            user_input = r.recognize_google(audio, language = 'en-in')
            print(f"user said: ",{user_input})
        except sr.RequestError:
            speak("Please say again, I was unable to recognize....")
        return None

def generate_response(prompt):
    os.environ['HUGGINGFACE_HUB_TOKEN'] = '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'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=150, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def main():
    print("Welcome to your voice-activated virtual assistant Jaggu!")
    wish()
        
    while True:
        user_input = listen_to_voice()
        if user_input is None:
            speak("I'm here to help you with anything you need.")
            continue
        elif user_input.lower() in ["exit", "quit", "stop"]:
            speak("Exiting...")
            break
        elif "open notepad" in user_input.lower():
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        elif "open google" in user_input.lower():
            npath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)
        elif "open internet explorer" in user_input.lower():
            npath = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
            os.startfile(npath)
        elif "open youtube" in user_input.lower():
            webbrowser.open("youtube.com")
        elif "open spotify" in user_input.lower():
            try:
                subprocess.Popen(["spotify"])
                print("Opening Spotify...")
            except FileNotFoundError:
                print("Spotify application not found.")
        elif "open instagram" in user_input.lower():
            webbrowser.open("https://www.instagram.com/")
        elif "the time" in user_input.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif "open code" in user_input.lower():
            codePath = "C:\\Users\\Kanishk\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        else:
            llama_response = generate_response(user_input)
            print(f"newJarvis Response: {llama_response}")
            speak(llama_response)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")


'''
import speech_recognition as sr
import torch
import pyttsx3
import datetime
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig
import webbrowser
import subprocess


# Define the model name
model_name = "C:\\codes\\llama1B\\" 

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning....")
    elif hour < 18:
        speak("Good afternoon....")
    else:
        speak("Good evening....")
    speak("I am your virtual assistant Jaggu, please tell me how can I help you.")

def listen_to_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Recognizing....")
            user_input = r.recognize_google(audio, language = 'en-in,hindi')
            print(f"user said: ",{user_input})
        except sr.RequestError:
            speak("Please say again, I was unable to recognize....")
        return None

def generate_response(prompt):
    os.environ['HUGGINGFACE_HUB_TOKEN'] = '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'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=150, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def main():
    print("Welcome to your voice-activated virtual assistant Jaggu!")
    wish()
        
    while True:
        user_input = listen_to_voice()
        if user_input is None:
            continue
            # Generate response using LLaMA
        llama_response = generate_response(user_input)
        print(f"newJarvis Response: {llama_response}")
        speak(llama_response)
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    while True:
        user_input = listen_to_voice()
        if user_input is None:
            llama_response = generate_response(user_input)
            print(f"newJarvis Response: {llama_response}")
            speak(llama_response)
            continue
        elif "open notepad" in user_input:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        elif "open google" in user_input:
            npath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)
        elif "open internet explorer" in user_input:
            npath = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
            os.startfile(npath)
        elif "open youtube" in user_input:
            webbrowser.open("youtube.com")
        elif "open spotify" in user_input:
            try:
                subprocess.Popen(["spotify"])
                print("Opening Spotify...")
            except FileNotFoundError:
                print("Spotify application not found.")
        elif "open instagram" in user_input:
            webbrowser.open("https://www.instagram.com/")
        elif "the time" in user_input:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif "open code" in user_input:
            codePath = "C:\\Users\\Kanishk\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "exit" in user_input:
                speak("Exiting...")
                break
'''
