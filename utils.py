import wikipedia
import pyttsx3
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from threading import Event, Thread

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
engine = pyttsx3.init()
stop_event = Event()

def search_wikipedia(query):
    try:
        wikipedia.set_lang("en")
        summary = wikipedia.summary(query)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Page not found."
    except Exception as e:
        return f"An error occurred: {e}"

def analyze_text(text):
    scores = sia.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return 'Positive'
    elif scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def speak(text):
    if not stop_event.is_set():
        def run_engine():
            engine.say(text)
            engine.runAndWait()
        Thread(target=run_engine).start()

def speak_insights(insights):
    if stop_event.is_set():
        return
    def run_engine():
        for insight in insights:
            if stop_event.is_set():
                break
            engine.say(insight)
            engine.runAndWait()
    Thread(target=run_engine).start()

def generate_insights(df):
    insights = []
    insights.append(f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.")
    for col in df.select_dtypes(include=['number']).columns:
        mean_val = df[col].mean()
        median_val = df[col].median()
        std_val = df[col].std()
        insights.append(f"Column '{col}' - Mean: {mean_val:.2f}, Median: {median_val:.2f}, Standard Deviation: {std_val:.2f}.")
    return insights
