from flask import Flask, render_template, request
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import process

app = Flask(__name__) #craet flask app

# abbloud the traind models and larg data names for fregrnce
with open("model/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("model/tfidf_matrix.pkl", "rb") as f:
    tfidf_matrix = pickle.load(f)

perfume_names = pd.read_csv("model/perfume_names.csv")
perfume_names["Name_lower"] = perfume_names["Name"].str.lower()# remove the snsivety 

# store fregrnce , this can be changed depends on the store
def load_store_data():
    df = pd.read_csv("data/store_products.csv")
    df = df.dropna(subset=["Name", "Main Accords"])
    df["Name_lower"] = df["Name"].str.lower()
    return df

df_store = load_store_data()

#-----------------------------------------------------------------------------------------------------------

#the main route recive the data when the user sent it 
@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = None
    user_input = ""
     #recvive the textual inputs and prosses it to fregrnce list
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        input_list = [x.strip().lower() for x in user_input.split(",") if x.strip()]
        all_perfumes = perfume_names["Name_lower"].tolist()
        #when the user write fregnens name not correct, this will correct it usin RappidFuzz
        corrected = []
        for name in input_list:
            match, score, _ = process.extractOne(name, all_perfumes)
            if score >= 65:
                corrected.append(match)
        #take all matches of the fregnens and calculate the average using TF-IDF (user taste)
        matched = perfume_names[perfume_names["Name_lower"].isin(corrected)]

        if not matched.empty:
            input_vectors = tfidf_matrix[matched.index]
            avg_vector = input_vectors.mean(axis=0).reshape(1, -1)
            # compare with the store fregnens (convert the store discription to vector and calc the simlirty with the users taste then return the hiest match)
            store_vectors = vectorizer.transform(df_store["Main Accords"].astype(str))
            similarities = cosine_similarity(avg_vector, store_vectors).flatten()
            df_store["Similarity"] = similarities

            result = df_store[~df_store["Name_lower"].isin(corrected)]
            recommendations = result.sort_values(by="Similarity", ascending=False).head(1)
    #show the html and return the best fregnens and what user enterd
    return render_template("index.html",
                           recommendations=recommendations,
                           user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
