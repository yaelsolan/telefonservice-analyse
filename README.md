# Telefonservice-Analyse

Dieses Projekt analysiert Kundenanfragen bei einem Telefonanbieter mithilfe von Natural Language Processing (NLP).

## Ziel
Das System soll automatisch:
- Anfragen klassifizieren (z. B. Vertrag, technische Störung, Kündigung)
- die Stimmung der Nachricht erkennen (positiv / neutral / negativ)
- passende Antwortvorschläge generieren

## Technologien
- Python 3
- pandas, scikit-learn
- einfache Textverarbeitung mit `re` und `string`
- Gradio (für eine interaktive Demo-Oberfläche)

## Beispiel-Anwendung
Ein Kunde schreibt:  
„Mein Internet funktioniert seit gestern nicht mehr.“

→ Klassifikation: technische Störung  
→ Stimmung: negativ  
→ Antwortvorschlag:  
„Wir bedauern die Unannehmlichkeiten. Unser technisches Team prüft das Problem und meldet sich umgehend.“

## Status
Projektstart: Mai 2025  
Status: In Entwicklung
