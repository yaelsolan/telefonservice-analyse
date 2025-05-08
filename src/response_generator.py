# src/response_generator.py

class ResponseGenerator:
    def __init__(self):
        self.responses = {
            "Störung": (
                "Wir bedauern die Unannehmlichkeiten. "
                "Unser technisches Team prüft das Problem und meldet sich umgehend."
            ),
            "Kündigung": (
                "Es tut uns leid, dass Sie kündigen möchten. "
                "Bitte beachten Sie unsere Kündigungsfristen in Ihrem Vertrag."
            ),
            "Vertrag": (
                "Gerne helfen wir Ihnen weiter. "
                "Was genau möchten Sie zu Ihrem Vertrag wissen?"
            ),
            "Rechnung": (
                "Bitte beachten Sie, dass Ihre letzte Rechnung im Kundenportal einsehbar ist. "
                "Bei Fragen stehen wir gerne zur Verfügung."
            ),
            "Allgemein": (
                "Vielen Dank für Ihre Nachricht. "
                "Unser Kundenservice wird sich zeitnah bei Ihnen melden."
            )
        }

    def generate(self, category):
        return self.responses.get(category, self.responses["Allgemein"])

# Beispiel
if __name__ == "__main__":
    generator = ResponseGenerator()
    print(generator.generate("Störung"))
    print(generator.generate("Vertrag"))
    print(generator.generate("Unbekannt"))  # Fallback
