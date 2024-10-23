import speech_recognition as sr
import webbrowser
from utils import search_wikipedia, analyze_text, speak_insights, stop_event

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
                webbrowser.open("http://localhost:8501")
                speak_insights(["Generating insights. Please check the browser for detailed analysis."])
            elif 'search' in text.lower():
                query = text.lower().replace("search", "").strip()
                speak_insights([f"Searching Wikipedia for {query}"])
                summary = search_wikipedia(query)
                print("Wikipedia Summary:", summary)
                speak_insights([summary])
            elif 'open youtube' in text.lower():
                webbrowser.open("https://www.youtube.com")
                speak_insights(["Opening YouTube"])
            elif 'open github' in text.lower():
                webbrowser.open("https://www.github.com")
                speak_insights(["Opening GitHub"])
            elif 'stop' in text.lower():
                stop_event.set()  # Signal to stop the TTS

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
