# Import necessary libraries
import spacy
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import uvicorn
import logging
import joblib

# Initialize Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load the pre-trained Named Entity Recognition (NER) model
nlp = spacy.load("en_core_web_sm")

# Initialize FastAPI application
app = FastAPI()

# Define the request format
class TextRequest(BaseModel):
    text: str

# Define the prediction endpoint
@app.post("/predict")
def predict_entities(request: TextRequest):
    """
    Extract named entities from the given text.
    """
    try:
        doc = nlp(request.text)
        entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
        return {"entities": entities}
    except Exception as e:
        logging.error(f"Error processing text: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Run the API
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
