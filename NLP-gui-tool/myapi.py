import nlpcloud

class Api:
    def __init__(self):
        # Client for sentiment analysis
        self.sentiment_client = nlpcloud.Client(
            "distilbert-base-uncased-finetuned-sst-2-english",
            "2e819f38661d44d49409c0fcda4a5982fa586c92",
            gpu=False
        )

        # Client for Named Entity Recognition
        self.ner_client = nlpcloud.Client(
            "en_core_web_lg",  # spaCy large English
            "2e819f38661d44d49409c0fcda4a5982fa586c92",
            gpu=False
        )

        self.client_ld = nlpcloud.Client("python-langdetect", "2e819f38661d44d49409c0fcda4a5982fa586c92", gpu=False)


    def sentiment_analysis(self, text):
        return self.sentiment_client.sentiment(text)

    def ner(self, text, searched_entity=None):
        if searched_entity:
            return self.ner_client.entities(text, searched_entity=searched_entity)
        return self.ner_client.entities(text)
    

    def language_detection(self, text):
        """
        Detects the language of the given text.
        """
        try:
            result = self.client_ld.langdetection(text)
            return result
        except Exception as e:
            return {"error": str(e)}



