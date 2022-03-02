from ctypes import sizeof
from random import random
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0])       # use [1] for female voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I am Naruto, How may I help you?")


# function to take microphone inputs
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Please say again...")
        return "None"

    return query

if __name__=="__main__":
    wishme()
    while True:
        query = takecommand().lower()

        # logic
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'play music' in query:
            music_dir = "D:\\SNIPER MKS"
            songs = os.listdir(music_dir)
            random_no = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[random_no]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, Right now the time is  {strTime}")

        elif 'code' in query:
            codePath = "C:\\Users\\mohit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)