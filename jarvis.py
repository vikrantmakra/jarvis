import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from gtts import gTTS
import winsound
from pygame import mixer

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour

    if hour>=0 and hour<12:
        speak("Good Morning")
    if hour>=12 and hour<19:
        speak("Good Afternoon")
    if hour>=19 and hour<24:
        speak("Good Night")
    speak("I am Jatt how may i help you")

def wishHin():
    mixer.init()
    mixer.music.load("greet.mp3")
    mixer.music.play()
    

def choosLang():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Eng or Hin")
        print("Listning....")
        r.pause_threshold =1
        audio=r.listen(source)
        print("Recogonising...")
        query=r.recognize_google(audio,language="en-in")
        return query


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold =1
        audio=r.listen(source)
    
    try:
        print("Recogonising...")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        print("please say that again")
        return "None"

    return query

if __name__ == "__main__":
    
    wishMe()
    while True:
           
            query=takeCommand().lower()

            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                print(results)
                speak("according to Wikipedia")
                speak(results)
            elif "open youtube" in query:
                webbrowser.open("youtube.com")

            elif "open google" in query:
                webbrowser.open("google.com")
        
            elif "open stack overflow" in query:
                webbrowser.open("stackoverflow.com")
            
            elif "open code" in query:
                path = "C:\\Users\\CSC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)
            elif "the time" in query:
                hour=datetime.datetime.now().strftime("%H:%M:%S")
                speak(hour)
            elif "who are you" in query:
                speak("I am jatt ")
       