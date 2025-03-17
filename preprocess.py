import re
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Tokenize and lowercase
    return " ".join(tokens)  # Convert list of words back into a string
