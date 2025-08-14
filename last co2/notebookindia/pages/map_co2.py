import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import os

def show_map_co2():
    st.title("🛰️ Visualisation de l'empreinte CO₂ par bâtiment - IIT Delhi")

    @st.cache_data
    def load_data():
    # Obtenir le chemin absolu du fichier KML
        current_dir = os.path.dirname(__file__)
        kml_path = os.path.abspath(os.path.join(current_dir, "campus_iit_delhi.kml"))

        if not os.path.exists(kml_path):
            st.error(f"❌ Fichier KML introuvable : {kml_path}")
            st.stop()

    # Charger les polygones du campus
        gdf = gpd.read_file(kml_path, driver="KML")

    # Charger les données CO₂
        csv_path = os.path.abspath(os.path.join(current_dir, "..", "data", "daily_energy_co2_india.csv"))
        if not os.path.exists(csv_path):
            st.error(f"❌ Fichier CSV introuvable : {csv_path}")
            st.stop()
        df = pd.read_csv(csv_path, parse_dates=["date"])
        df["date"] = df["date"].dt.date

        return gdf, df

    gdf, df = load_data()

    gdf["Name"] = gdf["Name"].str.strip()
    gdf_poly = gdf[gdf.geometry.geom_type == "Polygon"]
    gdf_point = gdf[gdf.geometry.geom_type == "Point"]
    df["date"] = pd.to_datetime(df["date"]).dt.date
    selected_date = st.sidebar.selectbox("🕒 Choisir une date :", sorted(df["date"].unique()))
    filtered_df = df[df["date"] == selected_date]

    to_col = {
        "Boys main": "BH_co2_kg",
        "SRB": "SRB_co2_kg",
        "Girls main": "GH_co2_kg",
        "Lecture": "LCB_co2_kg",
        "Library": "LB_co2_kg",
        "Dinnig": "DB_co2_kg",
        "OLD Boys H": "BH_bac_co2_kg",
        "OLD GIRLS H": "GH_bac_co2_kg"
    }

    to_thresholds = {
        "BH_co2_kg":      [336.61, 405.08, 478.16],
        "SRB_co2_kg":     [194.02, 246.10, 279.93],
        "GH_co2_kg":      [144.75, 164.39, 183.10],
        "LCB_co2_kg":     [0.00, 11.45, 29.46],
        "LB_co2_kg":      [136.80, 175.77, 235.99],
        "DB_co2_kg":      [401.77, 488.18, 566.80],
        "BH_bac_co2_kg":  [266.32, 299.07, 426.23],
        "GH_bac_co2_kg":  [130.03, 153.72, 174.76]
    }

    def classify(val, thresholds):
        if pd.isna(val): return "no_data"
        if val <= thresholds[0]: return "low"
        if val <= thresholds[1]: return "medium"
        if val <= thresholds[2]: return "high"
        return "very_high"

    tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
    attr = 'Tiles © Esri, USDA, USGS...'
    m = folium.Map(location=[28.5450, 77.2732], zoom_start=17, tiles=tiles, attr=attr)

    color_map = {
        "very_high": "#d73027",
        "high": "#fc8d59",
        "medium": "#fee08b",
        "low": "#91cf60",
        "no_data": "gray"
    }

    for _, row in gdf_poly.iterrows():
        name = row["Name"]
        geom = row["geometry"]
        co2_col = to_col.get(name)
        thresholds = to_thresholds.get(co2_col)

        if co2_col and thresholds:
            co2_value = filtered_df[co2_col].values[0] if not filtered_df.empty else None
            level = classify(co2_value, thresholds)
            color = color_map[level]
            folium.GeoJson(
                data=geom.__geo_interface__,
                style_function=lambda feat, col=color: {
                    "fillColor": col,
                    "color": "black",
                    "weight": 1,
                    "fillOpacity": 0.6
                },
                tooltip=f"{name} - {co2_value:.1f} kg CO₂" if co2_value else name
            ).add_to(m)

    for _, row in gdf_point.iterrows():
        name = row["Name"]
        geom = row["geometry"]
        co2_col = to_col.get(name)
        thresholds = to_thresholds.get(co2_col)

        if co2_col and thresholds:
            co2_value = filtered_df[co2_col].values[0] if not filtered_df.empty else None
            level = classify(co2_value, thresholds)
            color = color_map[level]
            folium.CircleMarker(
                location=[geom.y, geom.x],
                radius=8,
                color="black",
                fill=True,
                fill_color=color,
                fill_opacity=0.9,
                tooltip=f"{name} - {co2_value:.1f} kg CO₂" if co2_value else name
            ).add_to(m)

    st.subheader(f"📆 Date sélectionnée : {selected_date.strftime('%Y-%m-%d')}")
    st_folium(m, width=1000, height=600)
    st.markdown("---")
    st.markdown("🧠 Les couleurs représentent les niveaux de CO₂ par bâtiment en fonction de la consommation journalière.")
