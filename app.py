# app.py

import gr.Interface as gr
from src.preprocessing import clean_text
from src.classification import TextClassifier
from src.response_generator import ResponseGenerator

# Initialisierung
classifier = TextClassifier()
response_gen = ResponseGenerator()

# Beispiel-Daten zum Training
train_texts = [
    "Ich möchte meinen Vertrag kündigen.",
    "Mein Internet funktioniert nicht.",
    "Wie hoch ist meine letzte Rechnung?",
    "Ich habe Fragen zu meinem Tarif.",
    "Mein Router blinkt rot und funktioniert nicht."
]
train_labels = [
    "Kündigung",
    "Störung",
    "Rechnung",
    "Vertrag",
    "Störung"
]

classifier.train(train_texts, train_labels)

# Einfache Stimmungsanalyse auf Wortebene
def detect_sentiment(text):
    negative_words = ["nicht", "kein", "schlecht", "Problem", "Störung"]
    positive_words = ["danke", "zufrieden", "gut", "schnell"]

    text_lower = text.lower()
    if any(word in text_lower for word in negative_words):
        return "negativ"
    elif any(word in text_lower for word in positive_words):
        return "positiv"
    else:
        return "neutral"

# Gradio-Funktion
def analyse(text):
    category = classifier.predict(text)
    sentiment = detect_sentiment(text)
    response = response_gen.generate(category)

    return f"Kategorie: {category}\nStimmung: {sentiment}\n\nAntwortvorschlag:\n{response}"

# UI starten
demo = gr.Interface(fn=analyse, inputs="text", outputs=
