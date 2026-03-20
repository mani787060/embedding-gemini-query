# Google Gemini Text Embeddings & Retrieval
[![Google AI](https://img.shields.io/badge/API-Google%20Gemini-4285F4)](https://ai.google.dev/)
[![VectorSearch](https://img.shields.io/badge/AI-Semantic%20Search-green)](https://en.wikipedia.org/wiki/Vector_database)

## 🧠 Project Overview
This repository demonstrates the technical implementation of **Google Gemini Embeddings**. By converting text into dense numerical vectors, we move beyond keyword-based search to **Semantic Search**, allowing for a deeper mathematical understanding of context, intent, and relationship between documents.

---

## 🛠️ Key Technical Implementations

### 1. Vector Generation & Task Types
* **Model Selection:** Utilizing `text-embedding-004` for state-of-the-art vector representation.
* **Task-Specific Embeddings:** Implementing specific `task_type` parameters such as `RETRIEVAL_QUERY`, `RETRIEVAL_DOCUMENT`, and `CLUSTERING` to optimize vector orientation for specific use cases.

### 2. Semantic Retrieval Pipeline
* **Document Indexing:** Transforming a local knowledge base into a vector space.
* **Query Processing:** Converting natural language questions into query vectors and performing similarity matching against the indexed documents.

### 3. Mathematical Analysis
* **Cosine Similarity:** Measuring the angular distance between vectors to determine relevancy.
* **Dimensionality Management:** Handling the default 768-dimensional output for efficient storage and retrieval.

### 4. Enterprise Best Practices
* **Batch Processing:** Demonstrating how to embed multiple documents simultaneously for improved API performance.
* **Security:** Securely loading `GOOGLE_API_KEY` using `.env` files to prevent credential leakage.

---

## 💻 Tech Stack
* **Language:** Python
* **SDK:** `google-generativeai`
* **Mathematics:** NumPy, SciPy
* **Environment:** `python-dotenv`
* **Platform:** Jupyter Notebook / Google Colab
