import streamlit as st
import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination
import matplotlib.pyplot as plt
import os
import plotly.express as px


@st.cache_data
def load_data():
        # 🔧 Résolution du chemin absolu
        data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "df_final_project3.csv"))
        
        # ✅ Vérification
        if not os.path.exists(data_path):
            st.error(f"❌ Fichier introuvable : {data_path}")
            st.stop()

        return pd.read_csv(data_path, parse_dates=["timestamp"])
    

def simulateur_bayesien():
    st.title("🌱 Simulation d’un Scénario CO₂ avec Réseau Bayésien")

    df = load_data()

    # 🔹 Calcul occupation totale
    df['occupation_total'] = df[['ACB', 'BH', 'DB', 'GH', 'LB', 'LCB', 'SRB']].sum(axis=1)

    # 🔹 Prétraitement
    df = df[['hour', 'working_day', 'activity', 'temperature', 'humidity',
             'electricity_kwh', 'CO2_total', 'occupation_total']].dropna()

    df['temperature_cat'] = pd.cut(df['temperature'], bins=3, labels=["cold", "mild", "hot"])
    df['humidity_cat'] = pd.cut(df['humidity'], bins=3, labels=["dry", "normal", "humid"])
    df['electricity_cat'] = pd.cut(df['electricity_kwh'], bins=3, labels=["low", "medium", "high"])
    df['co2_cat'] = pd.cut(df['CO2_total'], bins=3, labels=["low", "medium", "high"])
    df['occupation_cat'] = pd.qcut(df['occupation_total'], q=3, labels=["low", "medium", "high"])
    df['working_day'] = df['working_day'].astype(str)
    df['hour'] = pd.cut(df['hour'], bins=4, labels=["night", "morning", "afternoon", "evening"])

    # 🔹 Réseau bayésien
    model = DiscreteBayesianNetwork([
        ("hour", "occupation_cat"),
        ("working_day", "occupation_cat"),
        ("occupation_cat", "electricity_cat"),
        ("temperature_cat", "electricity_cat"),
        ("humidity_cat", "electricity_cat"),
        ("electricity_cat", "co2_cat")
    ])
    model.fit(df, estimator=BayesianEstimator, prior_type="BDeu")
    infer = VariableElimination(model)

    # 🔹 Scénarios prédéfinis
    scenarios = {
        "Scénario 1 (Week-end matin doux)": {
            "hour": "morning", "working_day": "0", "temperature_cat": "mild", "humidity_cat": "normal", "electricity_cat": "low"
        },
        "Scénario 2 (Après-midi chaud en semaine)": {
            "hour": "afternoon", "working_day": "1", "temperature_cat": "hot", "humidity_cat": "humid", "electricity_cat": "high"
        },
        "Scénario 3 (Soirée froide en semaine)": {
            "hour": "evening", "working_day": "1", "temperature_cat": "cold", "humidity_cat": "dry", "electricity_cat": "medium"
        },
        "Scénario 4 (Nuit sèche week-end)": {
            "hour": "night", "working_day": "0", "temperature_cat": "cold", "humidity_cat": "dry", "electricity_cat": "low"
        },
        "Scénario 5 (Matin humide en semaine)": {
            "hour": "morning", "working_day": "1", "temperature_cat": "mild", "humidity_cat": "humid", "electricity_cat": "medium"
        },
        "Scénario 6 (Soirée chaude week-end)": {
            "hour": "evening", "working_day": "0", "temperature_cat": "hot", "humidity_cat": "normal", "electricity_cat": "high"
        },
        "Scénario 7 (Après-midi froid semaine)": {
            "hour": "afternoon", "working_day": "1", "temperature_cat": "cold", "humidity_cat": "normal", "electricity_cat": "medium"
        },
        "Scénario 8 (Matin très humide en semaine)": {
            "hour": "morning", "working_day": "1", "temperature_cat": "mild", "humidity_cat": "humid", "electricity_cat": "high"
        },
        "Scénario 9 (Soirée douce week-end faible conso)": {
            "hour": "evening", "working_day": "0", "temperature_cat": "mild", "humidity_cat": "normal", "electricity_cat": "low"
        },
        "Scénario 10 (Nuit chaude semaine haute conso)": {
            "hour": "night", "working_day": "1", "temperature_cat": "hot", "humidity_cat": "humid", "electricity_cat": "high"
        }
    }

    # 🔹 Choix du scénario
    selected_name = st.sidebar.selectbox("Choisissez un scénario", list(scenarios.keys()))
    selected_scenario = scenarios[selected_name]

    # 🔹 Inférence
    evidence = {
        "hour": selected_scenario["hour"],
        "working_day": selected_scenario["working_day"],
        "temperature_cat": selected_scenario["temperature_cat"],
        "humidity_cat": selected_scenario["humidity_cat"],
        "electricity_cat": selected_scenario["electricity_cat"]
    }
    result = infer.query(variables=["co2_cat"], evidence=evidence)

    # 🔹 Affichage
    st.subheader(f"📋 Détails du {selected_name}")
    st.json(evidence)

    st.subheader("📊 Résultat de la simulation")
    st.write(result)

    # 🔹 Graphique
    df_result = pd.DataFrame({
    "Classe CO₂": result.state_names["co2_cat"],
    "Probabilité": result.values
})

    fig = px.bar(df_result,
             x="Classe CO₂",
             y="Probabilité",
             text="Probabilité",
             color="Classe CO₂",
             color_discrete_sequence=["green"],
             title="Distribution des émissions de CO₂")

    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(width=800, height=650, showlegend=False)

    st.plotly_chart(fig, use_container_width=False)

# 🔹 Appel dans `app.py` ou autre fichier principal
if __name__ == "__main__":
    simulateur_bayesien()
