#  AI Fragrance Recommender Template

A beautifully engineered **AI-powered perfume recommendation system** that intelligently understands a user's favorite perfumes and finds the most compatible scent from a store's custom product catalog.

Built with love using **Python, Flask, NLP, and vector similarity modeling**.

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/a60747ce-a5ae-4d43-a294-31bf0873ed75" width="300" />
 <img src="https://github.com/user-attachments/assets/e7639b9d-7243-45ce-be18-cfc100fb9eae" width="300" />


</p>

---

## 🚀 Features

-  **Intelligent Scent Matching** using NLP-based vector embeddings  
-  **Fuzzy name correction** for user-entered perfume names  
-  **TF-IDF vectorization** for scent semantics  
-  **Cosine similarity ranking** between user preferences and store products  
-  **Top-1 recommendation** tailored to the user’s fragrance profile  
-  Designed to be a **template** easily adapted for any perfume business  
-  **Beautiful and elegant front-end** inspired by luxury design  

---

## 🧠 How It Works

This system goes beyond simple keyword matching — it **understands the essence of fragrances**.

1. The system is **pre-trained** on thousands of global perfumes, each converted into a high-dimensional semantic vector using **TF-IDF**.
2. When the user enters their favorite perfumes (e.g., “Miss Dior”, “Chanel Chance”), the system:
   - Applies **fuzzy logic** to correct any spelling mistakes  
   - Retrieves each perfume’s scent profile from the global dataset  
   - Computes a **mean scent vector** representing the user's preferences  
3. It then compares this scent vector against all local perfumes from the store (also vectorized) using **cosine similarity** — a powerful metric for semantic similarity.
4. The result:  
   👉 **The top 1 fragrance** from your store that best matches the user’s scent preferences, based on deep vector comparison.

---

## 📁 Folder Structure
project/
│
├── app.py 
├── templates/
│ └── index.html 
├── model/
│ ├── tfidf_vectorizer.pkl # Pre-trained TF-IDF vectorizer
│ ├── tfidf_matrix.pkl # Matrix of global perfumes
│ └── perfume_names.csv # Global perfume names + accords
├── data/
│ └── store_products.csv # Your store's perfume catalog
├── requirements.txt 

