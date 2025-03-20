

---

# **Smart Document Retrieval System**  

## **Overview**  
The **Smart Document Retrieval System** is a simple yet powerful search engine that retrieves the most relevant documents based on user queries. It utilizes **Information Retrieval (IR) techniques** such as **TF-IDF** and **cosine similarity** to rank and fetch documents efficiently with regards to the data present

---

## **Features**  
✅ **Text Preprocessing**: Tokenization, stopword removal, and stemming  
✅ **TF-IDF Vectorization**: Converts text into numerical vectors  
✅ **Cosine Similarity Matching**: Ranks documents based on query relevance  
✅ **Web Interface**: User-friendly search interface using **Flask or Streamlit**  
✅ **Result Ranking**: Displays the most relevant documents with similarity scores  

---

## **Tech Stack**  
- **Programming Language**: Python  
- **Libraries**:  
  - `scikit-learn` (TF-IDF & similarity)  
  - `nltk` (Natural Language Processing)  
  - `pandas` (Data Handling)  
  - `Flask` or `Streamlit` (Web UI)  
- **Data Source**: Wikipedia articles, news articles, or custom datasets  

---

## **Project Structure**  
```
📂 Smart-Document-Retrieval
│── 📂 data  
│   ├── documents.txt  (Text documents to search from)
│── 📂 static  (For UI assets if needed)
│── 📂 templates  (For HTML files if using Flask)
│── app.py  (Flask/Streamlit-based interface)
│── search_engine.py  (Core logic: TF-IDF and cosine similarity)
│── preprocess.py  (Text preprocessing: tokenization, stemming)
│── requirements.txt  (Dependencies)
│── README.md  (Project details)
```

---

## **Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/Smart-Document-Retrieval.git
cd Smart-Document-Retrieval
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Application**  

#### **Using Flask**
```bash
python app.py
```
Now, open **http://127.0.0.1:5000/** in your browser.  

#### **Using Streamlit**
```bash
streamlit run app.py
```

---

## **How It Works**  
1️⃣ **Preprocess Documents**:  
   - Converts text to lowercase  
   - Removes punctuation and stopwords  
   - Tokenizes words  
2️⃣ **Create TF-IDF Vectors**:  
   - Converts text into numerical representation  
3️⃣ **Compute Cosine Similarity**:  
   - Finds the most relevant documents  
4️⃣ **Display Top Results**:  
   - Shows ranked documents with similarity scores  

---

## **Example Usage**  
### **Input Query**  
> "Artificial Intelligence and Machine Learning"  

### **Output (Top 3 Results)**  
1️⃣ **"Introduction to AI and ML"** (Score: 0.87)  
2️⃣ **"Deep Learning Advances in AI"** (Score: 0.75)  
3️⃣ **"AI in Business and Healthcare"** (Score: 0.72)  

---

## **Future Enhancements**  
🔹 Implement **BM25 Ranking** instead of TF-IDF  
🔹 Add **FastAPI** for better scalability  
🔹 Use **BERT embeddings** for more accurate retrieval  

---

## **Contributing**  
Contributions are welcome! If you’d like to improve the project:  
1️⃣ Fork the repository  
2️⃣ Create a new branch (`feature-new-functionality`)  
3️⃣ Commit your changes and push  
4️⃣ Create a **Pull Request**  

---

## **License**  
This project is open-source and licensed under the **MIT License**.  

---

