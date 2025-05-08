# src/classification.py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


class TextClassifier:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def train(self, texts, labels):
        """
        Texte (Liste) und zugehörige Labels zum Trainieren übergeben.
        """
        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, labels)

    def predict(self, new_text):
        """
        Einen neuen Text klassifizieren.
        """
        X_new = self.vectorizer.transform([new_text])
        prediction = self.model.predict(X_new)
        return prediction[0]

# Beispielnutzung
if __name__ == "__main__":
    beispiel_texte = [
        "Ich möchte meinen Vertrag kündigen.",
        "Mein Internet funktioniert nicht.",
        "Wie hoch ist meine letzte Rechnung?",
        "Ich habe Fragen zu meinem Tarif.",
        "Mein Router blinkt rot und funktioniert nicht."
    ]
    beispiel_labels = [
        "Kündigung",
        "Störung",
        "Rechnung",
        "Vertrag",
        "Störung"
    ]

    classifier = TextClassifier()
    classifier.train(beispiel_texte, beispiel_labels)

    neue_frage = "Seit heute habe ich kein WLAN mehr."
    print("Kategorie:", classifier.predict(neue_frage))
