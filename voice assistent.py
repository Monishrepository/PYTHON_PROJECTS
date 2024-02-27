import speech_recognition as sr
import random
import webbrowser
#web browser
def webx(text):
    if "open youtube" in text.lower():
        webbrowser.open_new_tab("www.youtube.com")
    if "open instagram" in text.lower():
        webbrowser.open_new_tab("www.instagram.com")
    if "open gmail" in text.lower():
        webbrowser.open_new_tab("www.gmail.com")
    if "open facebook" in text.lower():
        webbrowser.open_new_tab("www.facebook.com")
    if "open gnc website" or "open guru nanak college website" in text.lower():
        webbrowser.open_new_tab("https://gurunanakcollege.edu.in/")
    else:
        print("try another")


def recognize_speech():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Say something:")

        try:
            audio = recognizer.listen(source, timeout=20)
            text = recognizer.recognize_google(audio)
            
            if "open" in text.lower():
                webx(text)
            
           

        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    recognize_speech()
