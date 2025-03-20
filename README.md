# Smart Document Retrieval System

## Overview
The **Smart Document Retrieval System** is a Python-based tool that allows users to search for relevant text documents stored in a specified folder. It uses **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity** to rank documents based on their relevance to the user's search query.

## Features
- Reads and processes all **.txt** files from a specified folder.
- Preprocesses text by **tokenizing, lowercasing, and removing stopwords**.
- Uses **TF-IDF vectorization** to represent documents numerically.
- Computes **Cosine Similarity** to rank documents based on relevance to the query.
- Returns the **top 5 most relevant documents**.

## Prerequisites
Ensure you have Python installed along with the required dependencies:
```sh
pip install numpy pandas scikit-learn nltk
```
Additionally, download the required NLTK data:
```sh
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## How It Works
1. The program **loads** all `.txt` files from a specified folder.
2. It **preprocesses** the text by removing stopwords, tokenizing, and converting to lowercase.
3. It **vectorizes** the documents using **TF-IDF**.
4. It **compares** the user's search query against the documents using **Cosine Similarity**.
5. It **returns** the top 5 most relevant documents based on similarity scores.

## Usage
1. Place your text documents in a folder (e.g., `documents`).
2. Run the script:
```sh
python script.py
```
3. Enter a search query when prompted.
4. The program will display the **top 5 relevant documents** along with their similarity scores.

## Example Output
```
Enter your search query: machine learning

Top Relevant Documents:
doc1.txt (Score: 0.8792)
doc3.txt (Score: 0.7654)
doc2.txt (Score: 0.6543)
doc5.txt (Score: 0.5432)
doc4.txt (Score: 0.4321)
```

## Folder Structure
```
Smart-Document-Retrieval/
│-- documents/            # Folder containing text documents
│-- script.py             # Main Python script
│-- README.md             # Project documentation
```

## License
This project is open-source and available for modification and distribution.

## Contribution
Feel free to contribute by submitting issues or pull requests.

---
Happy Searching! 🚀

