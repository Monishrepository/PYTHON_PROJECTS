import speech_recognition as sr
import random
import webbrowser
import wikipedia
import pyttsx3
from datetime import datetime
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greeting function
def greet():
    now = datetime.now()
    current_hour = now.hour
    if current_hour < 12:
        speak("Good morning! How can I assist you?")
    elif 12 <= current_hour < 18:
        speak("Good afternoon! How can I assist you?")
    elif 18 <= current_hour < 22:
        speak("Good evening! How can I assist you?")
    else:
        speak("Good night! How can I assist you?")

# Web browser and System Application
def open_website(text):
    if "open youtube" in text.lower():
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("opening youtube")
    elif "open instagram" in text.lower():
        speak("opening instagram")
        webbrowser.open_new_tab("https://www.instagram.com")
    elif "open gmail" in text.lower():
        speak("opening gmail")
        webbrowser.open_new_tab("https://www.gmail.com")
    elif "open facebook" in text.lower():
        speak("opening Facebook")
        webbrowser.open_new_tab("https://www.facebook.com")
    elif "open gnc website" in text.lower() or "open guru nanak college website" in text.lower():
        speak("opening guru nanak college website")
        webbrowser.open_new_tab("https://gurunanakcollege.edu.in/")
    elif "notepad" in text.lower():
        speak("notepad")
        os.system("notepad.exe")
    elif "calculator" in text.lower():
        speak("opening calculator")
        os.system("calc.exe")
    else:
        speak("Try another command.")

# Joke function
def tell_joke():
    jokes = [
        "This might make you laugh. How do robots eat guacamole? -- With computer chips.",
        "One joke, coming up! What is a sea monster’s favorite snack? -- Ships and dip.",
        "Why did the computer go to therapy? -- Because it had too many bytes of emotional baggage!",
        "Why don't scientists trust atoms? -- Because they make up everything!",
        "Why did the coffee file a police report? -- It got mugged!"
    ]
    rand_joke = random.choice(jokes)
    print("AI says:", rand_joke)
    speak("AI says: " + rand_joke)
# Wikipedia search
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        print("AI says:", result)
        speak("AI says: " + result)
    except wikipedia.exceptions.DisambiguationError as e:
        print(result)
        speak(f"Ambiguous term. Please be more specific. Suggestions: {', '.join(e.options)}")
    except wikipedia.exceptions.PageError:
        print(result)
        speak("Sorry, no information found.")

# Current time
def current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Current Time:", current_time)

# Shutdown and restart
def custom_commands(text):
    if "shutdown" in text.lower():
        speak("Shutting down. Goodbye!")
        os.system("shutdown /s /t 1")
    elif "restart" in text.lower():
        speak("Restarting. See you in a moment!")
        os.system("shutdown /r /t 1")

# Google API speech recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source)
            print("Say something:")

            try:
                audio = recognizer.listen(source, timeout=20)
                text = recognizer.recognize_google(audio)
                print(text)
                if "open" in text.lower():
                    open_website(text)
                elif "tell me a joke" in text.lower():
                    tell_joke()
                elif "wikipedia" or "what is" or "tell me about" in text.lower():
                    query = text.lower().replace("wikipedia", "").strip()
                    search_wikipedia(query)
                elif "date" and "time" in text.lower():
                    current_time()
                elif any(word in text.lower() for word in ["hi", "hello"]):
                    greet()
                elif any(word in text.lower() for word in ["shutdown", "restart", "reboot"]):
                    custom_commands(text)
                else:
                    speak("Try another command.")
            except sr.WaitTimeoutError:
                speak("Listening timed out. No speech detected.")
            except sr.UnknownValueError:
                speak("Could not understand audio.")
            except sr.RequestError as e:
                speak(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    greet()
    recognize_speech()
