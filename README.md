# 🎯 Objectifs du Projet

---

## **TARGET 1 : Évaluation Intelligente de l'Empreinte Carbone**
**Objectif**  
Modéliser et prévoir l'évolution de l'empreinte carbone.

**Description**  
Développement d'un système capable de **modéliser et prévoir l'évolution de l'empreinte carbone** d'un bâtiment d'entreprise à partir de :
- **Usages énergétiques** : consommation d'électricité, chauffage, refroidissement, etc.
- **Conditions climatiques** : température, humidité, ensoleillement, précipitations, etc.
- **Données contextuelles** : taux d'occupation, calendrier, événements spéciaux

**Technologies utilisées**  
- **Machine Learning** : modèles prédictifs avancés (RF, XGBoost, MLP, LSTM…)
- **Analyse temporelle** : séquences temporelles et saisonnalité
- **Intégration multi-sources** : fusion de données hétérogènes
- **Prédictions en temps réel** : mise à jour continue des modèles

---

## **TARGET 2 : Détection de Surconsommation Énergétique**
**Objectif**  
Détecter des situations de **surconsommation énergétique cachée**.

**Description**  
Exploitation de modèles d'apprentissage non supervisé pour identifier des anomalies :
- ✅ **Isolation Forest** : identification d'anomalies isolées
- ✅ **DBSCAN** : détection de regroupements inhabituels
- **Analyse des patterns** : mise en évidence de dérives énergétiques
- **Alertes automatiques** : notifications des surconsommations détectées

---

## **TARGET 3 : Classification des Usages Énergétiques**
**Objectif**  
Classifier les usages énergétiques selon les profils utilisateurs.

**Description**  
Dans le cadre de l'optimisation énergétique du campus de l'IIIT Delhi, l'objectif est de **classifier les usages énergétiques** des bâtiments en fonction des profils d'occupation :
- **Étudiants** : consommation pendant les heures de cours
- **Personnel administratif et technique** : usage pendant les heures de bureau
- **Week-ends et périodes de faible activité** : consommation minimale
- **Événements spéciaux** : pics de consommation exceptionnels

Cette classification permettra d’identifier les comportements propres à chaque profil et de mettre en place des stratégies ciblées de réduction et d'optimisation énergétique.

---
Le projet exploite le jeu de données énergétique du campus IIIT Delhi, accompagné d’un article de recherche décrivant la méthodologie d’acquisition et les métriques principales. Sur la branche main, trois notebooks distincts assurent le traitement et l’analyse correspondant aux trois cibles du projet : prédiction de l’empreinte carbone, détection de surconsommations et classification des usages. Parallèlement, la branche dashboard regroupe l’interface Streamlit qui centralise les résultats, visualisations interactives et modules IA issus des notebooks. Cette organisation facilite la séparation entre la phase analytique (branche main) et la phase de présentation interactive (branche dashboard), tout en permettant une évolution indépendante de chaque composant.
link : https://www.nature.com/articles/sdata201915
