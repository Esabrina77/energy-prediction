import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor

# Charger le modèle
model_path = './results/random_forest_model.pkl'  # Chemin vers votre modèle
model = joblib.load(model_path)

# Charger les données nettoyées
data_path = './data/prepared/model_data.csv'
data = pd.read_csv(data_path)

# Titre de l'application
st.title("Prédiction de Consommation Énergétique")

# Sélection de la ville
st.subheader("Sélectionnez une ville")
villes_disponibles = ['Toulouse']  # Vous pouvez ajouter plus de villes
ville = st.selectbox("Ville :", villes_disponibles)

# Inputs utilisateur
st.subheader("Entrez les paramètres météorologiques pour la prédiction")
temperature = st.number_input("Température (°C)", value=15.0)
humidity = st.number_input("Humidité (%)", value=50.0)
pressure = st.number_input("Pression au niveau de la
