#  AI Fragrance Recommender Template

A smart, plug-and-play fragrance recommendation system built with Flask, designed for perfume stores and brands. Users enter their favorite global perfumes, and the system suggests the most similar products from the local store catalog based on scent profile analysis.

 <img src=" https://github.com/user-attachments/assets/a60747ce-a5ae-4d43-a294-31bf0873ed75" width="400" hight="400">
---

## 🚀 Features

-  **Intelligent Matching** using TF-IDF + cosine similarity.
-  **Smart correction** of misspelled perfume names.
-  **Ready for deployment** as a template on any perfume brand.
-  **Brand integration** with customizable catalog.
-  **Elegant, modern frontend** with luxurious design.

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

It's not guessing. It's semantic reasoning across scent dimensions.
---

## 📁 Folder Structure


 
 

