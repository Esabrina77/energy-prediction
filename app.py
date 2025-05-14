import pandas as pd
import joblib
import streamlit as st
import requests
from datetime import datetime

# Charger le modèle et les features utilisés à l'entraînement
model = joblib.load('model.pkl')
features = joblib.load('features.pkl')

# Clé API OpenWeatherMap (ta clé personnelle)
API_KEY = "b48afb88d917d167c89d5c2ab61dd09a"

# Fonction pour récupérer la météo actuelle via l'API
def get_current_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        st.error(f"Erreur API météo : {data.get('message', 'Erreur inconnue')}")
        return None

    weather_data = {
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'pressure_sea_level': data['main']['pressure'],
        'wind_direction': data['wind']['deg'],
        'wind_speed': data['wind']['speed'],
        'min_soil_temp': data['main'].get('temp_min', data['main']['temp'])  # fallback si temp_min non dispo
    }
    return weather_data

# Enrichissement des features de la date
def enrich_date(date):
    date = pd.to_datetime(date)
    return {
        'month': date.month,
        'day_of_week': date.weekday(),
        'is_weekend': int(date.weekday() >= 5)
    }

# Fonction de prédiction
def predict_consumption_for_date(city_name, date_str):
    meteo = get_current_weather(city_name)
    if meteo is None:
        return None

    date_info = enrich_date(date_str)
    full_input = {**meteo, **date_info}
    X_input = pd.DataFrame([full_input])[features]
    prediction = model.predict(X_input)[0]
    return prediction

# Interface utilisateur Streamlit
st.set_page_config(page_title="Prédiction Énergie Toulouse", page_icon="⚡")
st.title('🔌 Prédiction de la consommation énergétique')

st.markdown("Prédit la consommation énergétique d’une ville à une date donnée, en se basant sur la météo réelle.")

# Choix utilisateur
date_input = st.date_input("🗓️ Choisissez une date", datetime.today())
city_input = st.text_input("🏙️ Entrez la ville", "Toulouse")

if st.button("Prédire la consommation"):
    prediction = predict_consumption_for_date(city_input, date_input)

    if prediction is not None:
        # Prendre la valeur absolue pour éviter les prédictions négatives
        prediction_abs = abs(prediction)

        # Convertir en milliers de kWh et arrondir à 3 décimales
        prediction_kwh = round(prediction_abs / 1000, 3)

        st.success(f"✅ Consommation prédite à {city_input} le {date_input.strftime('%d/%m/%Y')} : **{prediction_kwh:,.3f} kWh**")



