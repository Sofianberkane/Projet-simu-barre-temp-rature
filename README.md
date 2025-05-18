# 🔥 Simulation Numérique de l'Échauffement d'une Barre Métallique

Ce projet contient deux scripts Python permettant de visualiser l'évolution de la température dans une barre métallique chauffée à une extrémité, dans deux contextes : - **Régime stationnaire** : comparaison entre simulation numérique et solution analytique. - **Régime transitoire** : visualisation de l’évolution temporelle de la température.

## 📁 Structure des fichiers

├── regime_stationnaire.py   # Visualisation des données à l'équilibre  
├── regime_transitoire.py    # Visualisation des données en fonction du temps  
├── resultats.txt            # Données numériques (alu, cuivre, fer, eau)  
├── pos0.txt, posR.txt       # Données transitoires à y = 0 et y = R

## 🧪 1. `regime_stationnaire.py`

### ▶️ Description :  
Ce script :  
- charge des résultats simulés pour différents matériaux (aluminium, cuivre, fer, eau),  
- compare les températures à différentes positions radiales de la barre,  
- superpose la solution théorique analytique pour valider la simulation numérique.

### 📥 Données attendues :  
Fichiers `.txt` contenant 3 colonnes :  
Exemples de fichiers utilisés : `resultats.txt`, `resultats_cuivre.txt`, etc.

### 📈 Résultat :  
Un graphique affichant :  
- la température le long de la barre pour deux positions radiales,  
- la solution théorique :  
u(z) = (u₀ - u_A) · exp( -z * sqrt(2h / (Rλ)) ) + u_A

## ⏱ 2. `regime_transitoire.py`

### ▶️ Description :  
Ce script permet de visualiser :  
- l’évolution de la température dans le temps,  
- la propagation de la chaleur à différents instants,  
- l’impact de la conductivité thermique et du coefficient de convection.

### 📥 Données attendues :  
Fichiers `.txt` contenant des blocs de données séparés par des lignes vides :  
Chaque bloc représente un instant. Exemples : `posR.txt`, `posR_cond.txt`, `posR_conv.txt`.

### 📈 Résultat :  
- Un ensemble de courbes u(x) tracées à différents instants,  
- Possibilité de comparer différents matériaux ou conditions de convection.

## 🛠️ Dépendances

Les deux scripts nécessitent :

```bash
pip install numpy matplotlib
