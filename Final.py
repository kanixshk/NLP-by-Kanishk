import speech_recognition as sr
import torch
import pyttsx3
import datetime
import os
import webbrowser
import subprocess
from transformers import AutoTokenizer, AutoModelForCausalLM

# Define the model name
model_name = "C:\\codes\\llama1B\\" # Change this to the path of the model on your system

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
    speak("I am your virtual assistant, please tell me how can I help you.")

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
            user_input = r.recognize_google(audio, language='en-in')
            print(f"user said: ", {user_input})
        except sr.RequestError:
            speak("Please say again, I was unable to recognize....")
        return None

def generate_response(prompt):
    os.environ['HUGGINGFACE_HUB_TOKEN'] = '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'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=160, num_return_sequences=1,timeout=10)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def open_notepad():
    npath = "C:\\Windows\\System32\\notepad.exe"
    os.startfile(npath)

def open_google():
    npath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    os.startfile(npath)

def open_internet_explorer():
    npath = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
    os.startfile(npath)

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_spotify():
    try:
        subprocess.Popen(["spotify"])
        print("Opening Spotify...")
    except FileNotFoundError:
        print("Spotify application not found.")

def open_instagram():
    webbrowser.open("https://www.instagram.com/")

def tell_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak(f"Sir, the time is {strTime}")

def open_code():
    codePath = "C:\\Users\\HP\\OneDrive\\Desktop\\Visual Studio Code.lnk"
    os.startfile(codePath)
    
def open_calculator():
    subprocess.Popen("calc.exe")
    
def open_camera():
    subprocess.Popen("start microsoft.windows.camera:", shell=True)
    
def open_calendar():
    subprocess.Popen("start outlookcal:", shell=True)
    
def open_clock():
    subprocess.Popen("start ms-clock:", shell=True)
    
def open_copilot():
    subprocess.Popen("start copilot:", shell=True)

def open_microsoft_store():
    subprocess.Popen("start ms-windows-store:", shell=True)
    
def open_mail():
    subprocess.Popen("start outlookmail:", shell=True)
    
def open_whatsapp():
    subprocess.Popen("start whatsapp:", shell=True)

def open_powerpoint():
    subprocess.Popen("start powerpnt:", shell=True)
    
def open_word():
    subprocess.Popen("start winword:", shell=True)

def open_excel():
    subprocess.Popen("start excel:", shell=True)

def open_photos():
    subprocess.Popen("start ms-photos:", shell=True)
    
def open_settings():
    subprocess.Popen("start ms-settings:", shell=True)
    
def main():
    print("Welcome to your voice-activated virtual assistant Jaggu!")
    wish()
    
    # Command mapping
    command_mapping = {
        "open notepad": open_notepad,
        "open google": open_google,
        "open internet explorer": open_internet_explorer,
        "open youtube": open_youtube,
        "open spotify": open_spotify,
        "open instagram": open_instagram,
        "tell time": tell_time,
        "open code": open_code,
        "open calculator": open_calculator,
        "open camera": open_camera,
        "open calendar": open_calendar,
        "open clock": open_clock,
        "open copilot": open_copilot,
        "open microsoft store": open_microsoft_store,
        "open mail": open_mail,
        "open whatsapp": open_whatsapp,
        "open powerpoint": open_powerpoint,
        "open word": open_word,
        "open excel": open_excel,
        "open photos": open_photos,
        "open settings": open_settings
    }
        
    while True:
        user_input = listen_to_voice()
        if user_input is None:
            speak("I'm here to help you with anything you need.")
            continue
        elif user_input.lower() in ["exit", "quit", "stop"]:
            speak("Exiting...")
            break
        else:
            # Check if the user input matches any command in the mapping
            command_found = False
            for command, action in command_mapping.items():
                if command in user_input.lower():
                    action()
                    command_found = True
                    break
            
            if not command_found:
                llama_response = generate_response(user_input)
                print(f"newJarvis Response: {llama_response}")
                speak(llama_response)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
