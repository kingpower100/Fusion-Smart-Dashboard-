import streamlit as st
import random
import pandas as pd
import plotly.express as px

# 🔹 Définition des types d'agents
class Occupant:
    def __init__(self, actif=True):
        self.actif = actif

    def consommer(self, heure, jour):
        if not self.actif:
            return 0
        if heure in ["morning", "afternoon"] and jour == "1":
            return random.uniform(1.5, 2.0)
        elif jour == "0":
            return random.uniform(0.5, 1.0)
        return random.uniform(1.0, 1.5)

class Chauffage:
    def __init__(self, temperature):
        self.temperature = temperature

    def consommer(self):
        if self.temperature == "cold":
            return random.uniform(2.0, 3.0)
        elif self.temperature == "mild":
            return random.uniform(1.0, 1.5)
        else:
            return random.uniform(0.2, 0.5)

class Lumiere:
    def __init__(self, heure):
        self.heure = heure

    def consommer(self):
        if self.heure == "night":
            return random.uniform(1.0, 1.5)
        return random.uniform(0.3, 0.6)

# 🔸 Fonction principale de simulation
def simulateur_multi_agents():
    st.title("🧑‍🤝‍🧑 Simulateur Multi-Agents - Scénarios de Consommation & CO₂")

    # 🔹 Interface utilisateur
    st.sidebar.header("🎛️ Paramètres du scénario")
    hour = st.sidebar.selectbox("Période", ["night", "morning", "afternoon", "evening"])
    working_day = st.sidebar.selectbox("Jour ouvré", ["1 (Oui)", "0 (Non)"])
    temperature_cat = st.sidebar.selectbox("Température", ["cold", "mild", "hot"])
    nb_occupants = st.sidebar.slider("Nombre d’occupants actifs", 0, 100, 30)

    # 🔹 Initialisation des agents
    occupants = [Occupant(actif=True) for _ in range(nb_occupants)]
    chauffage = Chauffage(temperature=temperature_cat)
    lumiere = Lumiere(heure=hour)

    # 🔹 Simulation
    conso_total = sum([o.consommer(hour, working_day[0]) for o in occupants])
    conso_total += chauffage.consommer()
    conso_total += lumiere.consommer()

    # 🔹 Résultats numériques
    st.subheader("🔋 Résultat de la simulation multi-agents")
    st.metric("Consommation énergétique simulée", f"{conso_total:.2f} kWh")

    co2_total = conso_total * 0.819
    st.metric("Estimation des émissions CO₂", f"{co2_total:.2f} kg")

    # 🔹 Graphique (version Plotly Express)
    df_plot = pd.DataFrame({
        "Type": ["Consommation (kWh)", "Émissions (kg CO₂)"],
        "Valeur": [conso_total, co2_total]
    })

    fig = px.bar(
        df_plot,
        x="Type",
        y="Valeur",
        text="Valeur",
        color="Type",
        color_discrete_map={
            "Consommation (kWh)": "blue",
            "Émissions (kg CO₂)": "green"
        },
        title="Impact énergétique du scénario"
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(width=800, height=650, showlegend=False)

    st.plotly_chart(fig, use_container_width=False)

# 🔹 Appel de la fonction dans app.py ou script principal
if __name__ == "__main__":
    simulateur_multi_agents()
