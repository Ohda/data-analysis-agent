# Visualisation de Données Python

## Description
Un outil de visualisation de données interactif développé en Python, permettant de créer et manipuler des graphiques de manière dynamique.

## Fonctionnalités
- Création de visualisations de données interactives
- Interface utilisateur intuitive
- Support de multiples types de graphiques
- Manipulation des données en temps réel
- Sauvegarde et chargement des configurations

## Structure du Projet
```
.
├── app.py                         # Point d'entrée de l'application
├── data_dictionary.json          # Dictionnaire de données
├── Pages/
│   ├── backend.py               # Logique backend
│   ├── data_models.py           # Modèles de données
│   ├── python_visualisation_agent.py  # Agent de visualisation
│   └── graph/
│       ├── tools.py            # Outils pour les graphiques
│       ├── state.py            # Gestion d'état
│       └── nodes.py            # Définition des nœuds
```

## Installation
1. Clonez le dépôt :
```bash
git clone [url-du-repo]
```

2. Installez Poetry (si ce n'est pas déjà fait) :
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Installez les dépendances avec Poetry :
```bash
poetry install
```

## Utilisation
1. Activez l'environnement virtuel et lancez l'application :
```bash
poetry shell
python app.py
```

2. Accédez à l'interface via votre navigateur web à l'adresse indiquée.
