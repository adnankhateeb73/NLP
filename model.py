import spacy
import config

# Load the SpaCy model
nlp = spacy.load(config.NER_MODEL)

def extract_entities(text: str):
    """
    Extract named entities from the given text.
    """
    doc = nlp(text)
    return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
