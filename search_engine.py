from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import preprocess_text

# Sample documents (Replace with actual document loading logic)
documents = ["This is a sample document.", "Another example text."]

# Ensure each document is a string after preprocessing
documents = [preprocess_text(doc) for doc in documents]

# Check the type of the first document (Debugging)
print(type(documents[0]))  # Should print: <class 'str'>

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print("TF-IDF matrix created successfully!")
