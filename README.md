🌱 Energy Carbon Intelligence – IIIT Delhi


[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.37%2B-FF4B4B.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5%2B-F7931E.svg)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.1%2B-EB5E28.svg)](https://xgboost.ai/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16%2B-FF6F00.svg)](https://www.tensorflow.org/)
[![Pandas/Numpy](https://img.shields.io/badge/Pandas%20%26%20NumPy-2.2%2B-150458.svg)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.24%2B-3F4F75.svg)](https://plotly.com/)
[![Mistral AI](https://img.shields.io/badge/Mistral%20AI-7B%20%7C%208x7B-8000FF.svg)](https://mistral.ai/)
[![RAG](https://img.shields.io/badge/RAG-Retrieval--Augmented%20Generation-6f42c1.svg)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#license)




🧠 Project Overview

A complete data-driven and AI-powered framework for carbon footprint forecasting, energy overconsumption detection, and usage classification based on real-world energy datasets from the IIIT Delhi campus.

Built with Python (ML/AI + Streamlit dashboard), this project integrates time-series modeling, anomaly detection, and behavioral classification to support sustainable energy management and intelligent carbon evaluation.

⚙️ Tech Stack

Python 3.12+ • Streamlit • scikit-learn • XGBoost • TensorFlow • Pandas/Numpy • Plotly

Branches

main → Data analysis, ML models, notebooks

dashboard → Streamlit app (interactive visualization)

🧩 Targets & Objectives
🎯 TARGET 1 — Intelligent Carbon Footprint Evaluation

Goal:
Model and predict the evolution of a company building’s carbon footprint.

Methods:

Predictive ML models (Random Forest, XGBoost, MLP, LSTM)

Time-series modeling (seasonality, temporal dependencies)

Real-time updates with continuous learning

⚡ TARGET 2 — Energy Overconsumption Detection

Goal:
Detect hidden energy overconsumption patterns.

Methods:

Unsupervised anomaly detection (Isolation Forest, DBSCAN)

Behavioral pattern analysis & drift detection

Automated alert system for detected anomalies

👥 TARGET 3 — Energy Usage Classification

Goal:
Classify energy consumption by user profiles (students, staff, weekends, events).

Methods:

Temporal segmentation and clustering by occupancy

Labeling consumption patterns for behavior profiling

Adaptive recommendations for energy optimization

🔬 Dataset

Real-world energy management data from the IIIT Delhi campus.

📄 Reference: A real-world energy management dataset of IIIT Delhi

Published in Nature Scientific Data, 2019.

⚙️ Installation
# Clone the repository
git clone https://github.com/<username>/energy-carbon-intelligence-iiitd.git
cd energy-carbon-intelligence-iiitd

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)

# Install dependencies
pip install -r requirements.txt

🚀 Usage
🧠 Train a model
python -m src.eci.models.carbon_forecast --config configs/carbon_xgb.yaml

📊 Run the Streamlit dashboard (branch dashboard)
cd dashboard
pip install -r requirements.txt
streamlit run app.py

📄 License

This project is licensed under the MIT License — see the LICENSE
 file for details.

📞 Support

For questions, issues, or collaboration requests:

🐛 Create an issue in this repository

💬 Contact the development team: louay.fgaier@supcom.tn

📘 Check the individual README files in /notebooks and /dashboard for detailed documentation

🎯 Future Enhancements

🌍 Real-time Carbon Forecasting: live updates with retraining pipeline

⚡ Energy Efficiency Recommendations: rule-based + AI-generated insights

🔔 Anomaly Alerts: automated notifications for overconsumption events

🧠 Reinforcement Learning: adaptive control for optimal consumption

📊 Analytics Dashboard: multi-building CO₂ and consumption visualization

☁️ API Deployment: FastAPI backend for model serving and external integration

💡 About

Energy Carbon Intelligence – Empowering Smart, Sustainable Buildings ♻️🏢✨

Built with ❤️ using Python, Machine Learning, and Streamlit
to make energy data intelligent, transparent, and actionable.
