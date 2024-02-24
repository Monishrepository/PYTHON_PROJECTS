import speech_recognition as sr

def recognize_speech():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Say something:")

        try:
            audio = recognizer.listen(source, timeout=20)
            text = recognizer.recognize_google(audio)
            
            print("You said:", text)

        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    recognize_speech()
