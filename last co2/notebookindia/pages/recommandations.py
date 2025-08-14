import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

def show_energy_recommendations():
    @st.cache_data
    def load_data():
        current_dir = os.path.dirname(__file__)
        data_path = os.path.abspath(os.path.join(current_dir, "..", "data", "df_final_project3.csv"))
        if not os.path.exists(data_path):
            st.error(f"❌ Fichier introuvable : {data_path}")
            st.stop()
        return pd.read_csv(data_path, parse_dates=["timestamp"])

    def generer_recommandations(row):
        recommandations = []
        if row.get("CO2_total", 0) > 1000:
            recommandations.append("🔴 CO₂ élevé : réduire les équipements énergivores et ventiler.")
        if row.get("temperature", 0) > 26 and row.get("month", 0) in [6, 7, 8]:
            recommandations.append("🌞 Été chaud : éviter les pics de climatisation en milieu de journée.")
        if row.get("hour", 0) < 6 and row.get("electricity_kwh", 0) > 100:
            recommandations.append("🌙 Éclairage la nuit : automatiser avec des détecteurs de présence.")
        if row.get("occupation_total", 0) < 3 and row.get("electricity_kwh", 0) > 200:
            recommandations.append("👻 Bâtiment peu occupé mais énergivore : déconnecter équipements inutiles.")
        if row.get("humidity", 0) > 85:
            recommandations.append("💧 Humidité > 85% : activer la ventilation naturelle ou déshumidifier.")
        if "cluster" in row:
            if row["cluster"] == 2:
                recommandations.append("🕓 Cluster 2 : ajuster les horaires aux périodes creuses.")
            elif row["cluster"] == 3:
                recommandations.append("📊 Cluster 3 : vérifier les équipements en veille permanente.")
        if not recommandations:
            recommandations.append("✅ Aucune action urgente. Bon comportement énergétique.")
        return " | ".join(recommandations)

    st.title("📊 Scénarios & Recommandations Intelligentes")
    st.write("Recevez des recommandations ciblées basées sur les données énergétiques et climatiques.")

    df = load_data()
    df["occupation_total"] = df[["ACB", "BH", "DB", "GH", "LB", "LCB", "SRB"]].sum(axis=1)

    # ---- Sidebar ----
    st.sidebar.header("🔍 Filtres")
    if "usage" in df.columns:
        usages = df["usage"].dropna().unique().tolist()
        usage_filter = st.sidebar.multiselect("Usage", usages, default=usages)
        df = df[df["usage"].isin(usage_filter)]
    if "building" in df.columns:
        buildings = df["building"].dropna().unique().tolist()
        building_filter = st.sidebar.selectbox("Bâtiment", ["Tous"] + buildings)
        if building_filter != "Tous":
            df = df[df["building"] == building_filter]

    # ---- What-if Simulation ----
    st.subheader("⚙️ Simulation What-if : Réduction hypothétique")
    reduction = st.slider("Réduction % de consommation", 0, 50, 10, step=5)
    df["CO2_total_simul"] = df["CO2_total"] * (1 - reduction / 100)

    fig = px.line(df, x="timestamp", y=["CO2_total", "CO2_total_simul"],
                  labels={"value": "CO₂ (kg)", "timestamp": "Date"},
                  title=f"Impact d'une réduction de {reduction}% sur le CO₂")
    st.plotly_chart(fig, use_container_width=True)

    # ---- Alertes ----
    st.subheader("🔔 Alertes intelligentes")
    alerts = []
    if df["month"].isin([6, 7, 8]).any() and df["temperature"].mean() > 28:
        alerts.append("🔥 Canicule détectée : attention à la surconsommation.")
    if df["hour"].isin(range(0, 6)).any():
        alerts.append("🌃 Activité détectée la nuit : consommation anormale possible.")
    if df["CO2_total"].max() > 1500:
        alerts.append("📈 Pic de CO₂ très élevé : revoir les systèmes HVAC.")
    for alert in alerts:
        st.warning(alert)
    if not alerts:
        st.success("✅ Aucun comportement critique détecté.")

    # ---- Recommandations ----
    st.subheader("🧠 Recommandations personnalisées")
    df["recommandations"] = df.apply(generer_recommandations, axis=1)
    st.dataframe(df[["timestamp", "CO2_total", "CO2_total_simul", "recommandations"]].sort_values("timestamp").tail(15))

    # ---- Cluster summary ----
    if "cluster" in df.columns:
        st.subheader("📚 Recommandations moyennes par cluster")
        cluster_recs = df.groupby("cluster")["recommandations"].apply(lambda x: x.value_counts().index[0])
        st.table(cluster_recs.reset_index().rename(columns={"recommandations": "Recommandation principale"}))

    # ---- Rapport export ----
    st.download_button("📄 Télécharger le rapport", data=df.to_csv(index=False).encode("utf-8"),
                       file_name="rapport_recommandations.csv", mime="text/csv")
