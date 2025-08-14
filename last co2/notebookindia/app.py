import streamlit as st
# Configuration Streamlit - DOIT être la première commande Streamlit
st.set_page_config(page_title="Structure Énergétique", layout="wide")

import requests
import datetime
import pytz
import os
import importlib.util
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from PIL import Image
from pages.map_co2 import show_map_co2
from pages.campus_energy_network_graph import show_energy_network_graph
from pages.recommandations import show_energy_recommendations
from pages.simulateur_bayesien import simulateur_bayesien
from pages.simulateur_multi_agents import simulateur_multi_agents

# Configuration Streamlit - Masquer la navigation automatique
hide_pages_style = """
<style>
    /* Masquer la navigation automatique de Streamlit */
    section[data-testid="stSidebarNav"] {display: none;}
    
    /* Masquer la barre de recherche et suggestions */
    .stSearchBox {display: none;}
    .stSearchBox > div {display: none;}
    
    /* Masquer les suggestions de navigation */
    [data-testid="stSidebar"] [data-testid="stSidebarNav"] {display: none;}
    
    /* Masquer la barre de navigation en haut */
    header[data-testid="stHeader"] {display: none;}
    
    /* Masquer le menu hamburger */
    #MainMenu {visibility: hidden;}
    
    /* Masquer le footer */
    footer {visibility: hidden;}
    
    /* Masquer les éléments de navigation automatique */
    .stApp > header {display: none;}
    .stApp > footer {display: none;}
</style>
"""
st.markdown(hide_pages_style, unsafe_allow_html=True)
# Barre latérale
st.sidebar.title("🔧 Navigation")
page = st.sidebar.radio("Aller à :", [
    "🏠 Accueil",
    "🗺️ Carte CO₂",
    "📊 Recommandations",
    "🧠 Simulateur bayésien",
    "🤖 Simulateur multi-agents",
    "💬 Assistant IA"
])








# Page Accueil
if page == "🏠 Accueil":
    st.markdown("<h1 style='color:#FFFFFF;'>📊 Tableau de bord énergétique</h1>", unsafe_allow_html=True)
    st.markdown("Bienvenue sur le tableau de bord **Fusion Smart**, pour une gestion intelligente de l'énergie.", unsafe_allow_html=True)

    # Infos météo - IIT Delhi
    latitude = 28.5450
    longitude = 77.2732
    timezone = "Asia/Kolkata"

    try:
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}&longitude={longitude}"
            f"&current_weather=true"
            f"&hourly=relativehumidity_2m,shortwave_radiation"
            f"&timezone={timezone}"
        )
        response = requests.get(url, timeout=5)
        data = response.json()

        weather = data["current_weather"]
        temperature = weather["temperature"]
        windspeed = weather["windspeed"]
        weathercode = weather["weathercode"]

        tz = pytz.timezone(timezone)
        now = datetime.datetime.now(tz)
        local_time = now.strftime("%Y-%m-%d %H:%M")
        now_hour = now.replace(minute=0, second=0, microsecond=0).isoformat()
        now_iso = now.replace(minute=0, second=0, microsecond=0).isoformat()

        radiation = None

        if "hourly" in data and "time" in data["hourly"]:
            if now_iso in data["hourly"]["time"]:
                index = data["hourly"]["time"].index(now_iso)
                humidity = data["hourly"]["relativehumidity_2m"][index]

        weather_icons = {
            0: "☀️ Ciel clair",
            1: "🌤️ Peu nuageux",
            2: "⛅ Partiellement nuageux",
            3: "☁️ Couvert",
            45: "🌫️ Brouillard",
            48: "🌫️ Brouillard givrant",
            51: "🌦️ Bruine légère",
            53: "🌧️ Bruine modérée",
            55: "🌧️ Forte bruine",
            61: "🌦️ Pluie légère",
            63: "🌧️ Pluie modérée",
            65: "🌧️ Pluie forte",
            80: "🌦️ Averses légères",
            81: "🌧️ Averses modérées",
            82: "⛈️ Averses violentes",
        }
        weather_icon = weather_icons.get(weathercode, "N/A")

        st.subheader("📍 Météo en temps réel - IIT Delhi")
        st.write(f"L'IIT Delhi est un campus universitaire de pointe situé au cœur de New Delhi, intégrant de nombreux bâtiments académiques, résidentiels et de recherche. Grâce à ce tableau de bord, nous surveillons en temps réel la consommation énergétique et l'empreinte carbone de ses principales infrastructures.")
        st.write(f"🕒 **Heure locale :** {local_time}")
        st.write(f"🌡️ **Température :** {temperature} °C")
        st.write(f"💨 **Vent :** {windspeed} km/h")
        st.write(f"🌈 **Condition météo :** {weather_icon}")

     
        st.markdown("## 🏢 Structure énergétique du campus IIT Delhi")
        st.markdown("Visualisation des connexions entre transformateurs et bâtiments.")
        show_energy_network_graph()



        data_path = os.path.join(os.path.dirname(__file__), "data", "df_final_project3.csv")
        df = pd.read_csv(data_path, parse_dates=["timestamp"])

        df["datetime"] = df["timestamp"]

    # 2. Colonnes de consommation réelle par bâtiment (kWh)
        energy_label_map = {
    'BH_pow_kwh': "Boy's Dormitory Building",
    'BH_bac_pow_kwh': " OLD Boy's Dormitory ",
    'GH_pow_kwh': "Girl's Dormitory Building",
    'GH_bac_pow_kwh': " OLD Girl's Dormitory ",
    'DB_pow_kwh': "Dining Building",
    'LB_pow_kwh': "Library Building",
    'LCB_pow_kwh': "Lecture Building",
    'SRB_pow_kwh': "Facilities Building"
}
    # 3. Filtre de date
        st.sidebar.header("📅 Filtrer par période")
        date_min = df["datetime"].min().date()
        date_max = df["datetime"].max().date()
        date_range = st.sidebar.date_input("Plage de dates", [date_min, date_max])

    # 4. Sélection des bâtiments (consommation réelle)
        label_options = list(energy_label_map.values())
        selected_labels = st.sidebar.multiselect(
            "🏢 Sélectionner les bâtiments",
            options=label_options,
            default=label_options
        )

        selected_cols = [col for col, label in energy_label_map.items() if label in selected_labels]

        if not selected_cols:
            st.warning("⚠️ Veuillez sélectionner au moins un bâtiment.")
            st.stop()
    # 5. Filtrage par date
        df_filtered = df[
            (df["datetime"] >= pd.to_datetime(date_range[0])) &
            (df["datetime"] <= pd.to_datetime(date_range[1]))
        ]

    # 6. Format long pour affichage
        df_long = df_filtered[["datetime"] + selected_cols].melt(
            id_vars="datetime",
            value_vars=selected_cols,
            var_name="colonne",
            value_name="consommation_kWh"
        )
        df_long["bâtiment"] = df_long["colonne"].map(energy_label_map)
        SEUIL_KWH = 30  
    # 7. Graphique consommation par bâtiment
        st.title("🔌 Consommation électrique (kWh)")
        fig = px.line(
            df_long,
            x="datetime",
            y="consommation_kWh",
            color="bâtiment",
            title=" Consommation réelle (kWh) par bâtiment sélectionné",
            labels={"datetime": "Date/Heure", "consommation_kWh": "kWh"}
        )
        fig.add_hline(
            y=SEUIL_KWH,
            line_dash="dot",
            line_color="red",
            annotation_text="Seuil 30 kWh",
        annotation_position="top left"
        )
        st.plotly_chart(fig, use_container_width=True)
        
    # 8. Graphique CO₂ total
        st.subheader("📈 Émissions de CO₂ totales")
        fig2 = px.line(
            df_filtered,
            x="datetime",
            y="CO2_total",
            title="Émissions totales de CO₂ (kg)",
            labels={"datetime": "Date/Heure", "CO2_total": "CO₂ (kg)"}
        )
        fig2.add_hline(
            y=500,
            line_dash="dash",
            line_color="red",
            annotation_text="Seuil CO₂ : 500 kg",
            annotation_position="top left",
            
            )
        
        st.plotly_chart(fig2, use_container_width=True)
        #alerte 
        # ✅ Calcul des dépassements journaliers de CO₂
        df_daily_co2 = df_filtered[["datetime", "CO2_total"]].copy()
        df_daily_co2["date"] = df_daily_co2["datetime"].dt.date
        df_daily_sum = df_daily_co2.groupby("date")["CO2_total"].sum().reset_index()

# ✅ Vérifier les jours avec dépassement du seuil de 500 kg
       # ⚠️ Seuil d'alerte par heure
        SEUIL_CO2 = df_filtered["CO2_total"].quantile(0.95)

# ✅ Extraire la date et vérifier si au moins une heure dépasse le seuil dans la journée
        df_hourly = df_filtered[["datetime", "CO2_total"]].copy()
        df_hourly["date"] = df_hourly["datetime"].dt.date

# Vérifier les jours où au moins une valeur horaire > seuil
        depassements = df_hourly[df_hourly["CO2_total"] > SEUIL_CO2]
        jours_depassement = depassements["date"].unique()

# ✅ Affichage de l'alerte
        if len(jours_depassement) > 0:
            st.error(f"🚨 {len(jours_depassement)} jour(s) ont eu au moins 1 heure avec plus de {SEUIL_CO2} kg de CO₂.")
            with st.expander("📅 Voir les jours concernés"):
                df_jours = pd.DataFrame(jours_depassement, columns=["Date"])
            st.dataframe(df_jours)
        else:
            st.success("✅ Aucun dépassement horaire du seuil de CO₂ détecté.")


       

        #RADAR CHART  st.subheader("📡 Moyenne de consommation par bâtiment (radar chart)")

        # Calcul des moyennes
        moyennes = df_filtered[selected_cols].mean()
        labels = [energy_label_map[col] for col in selected_cols]
        values = moyennes.values.tolist()
        values += [values[0]]  # boucle pour fermer le polygone
        labels += [labels[0]]  # idem pour l’axe

# 2. Radar chart Plotly
        fig_radar = go.Figure()

        fig_radar.add_trace(go.Scatterpolar(
        r=values,
        theta=labels,
        fill='toself',
        name='Consommation moyenne',
        line=dict(color='royalblue')
        ))

        fig_radar.update_layout(
            polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, max(values) * 1.2]
        )
        ),
        title="⚡ Moyenne de consommation électrique par bâtiment (kWh)",
        showlegend=False
    )
        
# 3. Affichage Streamlit
        st.plotly_chart(fig_radar, use_container_width=True)
        # 📈 Métriques énergétiques
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="🏢 Bâtiments Connectés",
                value="9",
                delta="+2 cette année"
            )
        
        with col2:
            st.metric(
                label="⚡ Puissance Totale",
                value="2.5 MW",
                delta="+0.3 MW"
            )
        
        with col3:
            st.metric(
                label="🌱 Efficacité Énergétique",
                value="85%",
                delta="+5%"
            )
    except Exception as e:
        st.error("❌ Une erreur est survenue.")
        st.exception(e)
# Page Carte CO₂
elif page == "🗺️ Carte CO₂":
    show_map_co2()
elif page == "📊 Recommandations":
    show_energy_recommendations()
elif page == "🧠 Simulateur bayésien":
    simulateur_bayesien()

elif page == "🤖 Simulateur multi-agents":
    simulateur_multi_agents()
elif page == "💬 Assistant IA":
    try:
        # Import and run the energy assistant using the wrapper
        from energy_assistant_wrapper import run_energy_assistant_wrapper
        run_energy_assistant_wrapper()
        
    except ImportError as e:
        st.error(f"❌ Erreur d'importation de l'assistant IA: {str(e)}")
        st.info("💡 Assurez-vous que le projet energy-assistant est accessible depuis ce répertoire.")
        st.info(f"💡 Erreur détaillée : {str(e)}")
    except Exception as e:
        st.error(f"❌ Erreur lors de l'exécution de l'assistant IA: {str(e)}")
        st.exception(e)
