import pyttsx3
import speech_recognition as sr
import datetime
import os
import smtplib
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


#from text to speech convert krne ke liye function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#function to take command from the user
#function to convert speech to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshhold = 3
        audio = r.listen(source, timeout=3, phrase_time_limit=8)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = 'en-in,hindi')
        print(f"user said: ",{query})

    except Exception as e:
        speak("Please say again, i was unable to recognize....")
        return "none"
    return query


#to send mails
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("kanishkbainsla@gmail.com", "Mitthu@1502")
    server.sendmail("kanishkbainsla@gmail.com", to, content)
    server.close()


#function to wish the user
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning....")
    elif hour>=12 and hour<=18:
        speak("Good afternoon....")
    else:
        speak("Good Evening....")
    speak("I am Jarvis sir, please tell me how can i help you")




if __name__ == "__main__":
    wish()
    if 1:
        query = takecommand().lower()

        #logic building for tasks
        
        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        elif "open google" in query:
            npath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)
        elif "open internet explorer" in query:
            npath = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
            os.startfile(npath)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open spotify" in query:
            webbrowser.open("https://open.spotify.com/?flow_ctx=99afdbe8-8da3-4d15-97af-aa417f97a0d3%3A1727016309")
        elif "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif "open code" in query:
            codePath = "C:\\Users\\Kanishk\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "send a email" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=new")    
        
