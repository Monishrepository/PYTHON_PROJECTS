import pyttsx3 
import os
import speech_recognition as sr
import wikipedia
import webbrowser
import comtypes.client
import datetime

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    speak("good morning")
    speak("welcome")
def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("sollunga......")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recogonizing")
        query=r.recognize_google(audio,language='en-in')
        print(f"user say:(query)\n")
    except Exception as e :
        print("say again")
        return "None"
    return query
if __name__ == "__main__":
    wishme()
    while True:
        query = take().lower()
        if 'wikipedia' in query:
            speak('searching')
            query=query.replace("wikipedia"," ")
            result= wikipedia.summary(query,sentences)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open Facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open insta' or 'instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            
        
        
        
