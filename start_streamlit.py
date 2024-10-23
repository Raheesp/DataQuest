import speech_recognition as sr
import subprocess

import speech_recognition as sr
import os
import webbrowser
from utils import search_wikipedia, analyze_text,speak, stop_event

def open_application(application):
    if application == "YouTube":
        webbrowser.open("https://www.youtube.com")
    elif application == "GitHub":
        webbrowser.open("https://www.github.com")
    elif application == "Visual Studio Code":
        os.system("code")  # Ensure 'code' is in your PATH
    elif application == "Discord":
        os.system("start discord")  # Windows specific; adjust for other OSes
    else:
        speak(f"Application {application} not recognized.")

def listen_and_process():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            sentiment = analyze_text(text)
            print(f"Sentiment: {sentiment}")

            if 'generate insight' in text.lower():
                speak("Generating insights. Please check the browser for detailed analysis.")
                os.system('streamlit run main.py')

            elif 'search' in text.lower():
                query = text.lower().replace("search", "").strip()
                speak("Searching Wikipedia for " + query)
                summary = search_wikipedia(query)
                speak(summary)

            elif 'stop' in text.lower():
                stop_event.set()  # Signal to stop the TTS
            
            elif 'open' in text.lower():
                application = text.lower().replace("open", "").strip().title()
                speak(f"Opening {application}")
                open_application(application)

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

def listen_and_start_streamlit():
    while True:
        listen_and_process()

if __name__ == "__main__":
    listen_and_start_streamlit()


def listen_and_start_streamlit():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for 'generate insight' command...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            if 'generate insight' in text.lower():
                print("Starting Streamlit...")
                subprocess.Popen(["streamlit", "run", "main.py"])
            else:
                print("Command not recognized. Please say 'generate insight' to start the Streamlit app.")

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    listen_and_start_streamlit()
