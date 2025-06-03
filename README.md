#  AI Fragrance Recommender Template

A beautifully engineered AI-powered perfume recommendation system that intelligently understands a user's favorite perfumes and finds the most compatible scent from a store's custom product catalog.

Built with love using Python, Flask, NLP, and vector similarity modeling.


 
---
 <img src=" https://github.com/user-attachments/assets/a60747ce-a5ae-4d43-a294-31bf0873ed75" width="300" hight="300">

## 🚀 Features

 Intelligent Scent Matching using NLP-based vector embeddings.

 Fuzzy name correction for user-entered perfume names.

 TF-IDF vectorization for scent semantics.

 Cosine similarity ranking between user preferences and store products.

 Top-1 recommendation tailored to the user’s fragrance profile.

 Designed to be a template easily adapted for any perfume business.

 Beautiful and elegant front-end inspired by luxury design.
---

##  How It Works


This system goes beyond simple keyword matching — it understands the essence of fragrances.

1- The system is pre-trained on thousands of global perfumes, each converted into a high-dimensional semantic vector using TF-IDF.

2- When the user types in their favorite perfumes (e.g., “Miss Dior”, “Chanel Chance”), the system:

Uses fuzzy logic to correct any spelling mistakes.

Retrieves each perfume’s scent profile from the global dataset.

Converts the combination of input perfumes into a mean scent vector.

3- It then compares this scent vector against all local perfumes from the store (also vectorized) using cosine similarity — a powerful metric for understanding concept proximity in vector space.

4- The result: the top 1 fragrance from your catalog that best matches the user’s scent preferences, based on deep vector comparison.


---

## 📁 Folder Structure
project/
│
├── app.py                     # Flask backend logic
├── templates/
│   └── index.html             # Elegant front-end interface
├── model/
│   ├── tfidf_vectorizer.pkl   # Pre-trained TF-IDF vectorizer
│   ├── tfidf_matrix.pkl       # Matrix of global perfumes
│   └── perfume_names.csv      # Global perfume names + accords
├── data/
│   └── store_products.csv     # Your store's perfume catalog
├── requirements.txt           # All dependencies


 
 

