from sklearn.datasets import fetch_20newsgroups

# Load the 20 Newsgroups dataset
newsgroups = fetch_20newsgroups(subset="all", remove=("headers", "footers", "quotes"))

# Extract documents
documents = newsgroups.data

# Save to a text file for future use
with open("data/documents.txt", "w", encoding="utf-8") as f:
    for doc in documents:
        f.write(doc + "\n\n")

print("Dataset successfully saved in data/documents.txt")
