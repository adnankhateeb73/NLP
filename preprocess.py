import re

def clean_text(text: str) -> str:
    """
    Preprocesses input text by removing unwanted characters.
    """
    text = text.lower().strip()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    return text
