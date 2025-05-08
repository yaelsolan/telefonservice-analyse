# src/preprocessing.py

import re
import string

STOPWORDS = {
    "ich", "du", "er", "sie", "es", "wir", "ihr", "sie",
    "mein", "dein", "sein", "ihr", "unser", "euer", "nicht",
    "kein", "und", "oder", "aber", "dass", "weil", "wie", "was", "für", "mit"
}

def clean_text(text):
    """
    Bereinigt den Eingabetext:
    - Kleinbuchstaben
    - Entfernt Satzzeichen
    - Entfernt Stopwords
    - Gibt Liste von Wörtern zurück
    """
    # Kleinbuchstaben
    text = text.lower()

    # Satzzeichen entfernen
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)

    # In Wörter aufteilen
    words = text.split()

    # Stopwords entfernen
    cleaned = [word for word in words if word not in STOPWORDS]

    return cleaned

# Beispiel
if __name__ == "__main__":
    beispiel = "Mein Internet funktioniert seit gestern nicht mehr."
    print(clean_text(beispiel))
    # Ausgabe: ['internet', 'funktioniert', 'seit', 'gestern', 'mehr']
