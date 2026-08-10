# Actuariat Non-Vie — Modèle collectif du risque

**Cours :** Mathématiques Actuarielles — Master 2 IREF, Université de Bordeaux
**Co-auteur :** Robin Faidy (rapport)

## Objectif

Étudier la loi de la charge sinistrale totale `S` d'un portefeuille, dans un modèle collectif où :
- la fréquence des sinistres `N` suit une loi de Poisson `P(10)`
- la sévérité `X` de chaque sinistre suit une loi exponentielle `E(1/100)`

Trois méthodes sont comparées pour approcher la loi de `S` :
1. **Simulation Monte-Carlo** (100 000 tirages)
2. **Algorithme de Panjer** (récurrence exacte pour les lois composées)
3. **Convolution numérique** discrète

Le rapport calcule ensuite l'espérance, le quantile à 5 % et la VaR à 5 % de `S` par chaque méthode, et compare les écarts.

## Fichiers

- `Rapport_Modele_Collectif_Poisson_Exponentielle.pdf` — rapport complet (méthodologie, résultats, interprétation)
- `panjer_convolution_simulation.py` — script principal : simulation, Panjer, convolution, comparaison graphique
- `exercice5_modele_collectif.py` — variante avec calcul explicite de la densité de `S` par mélange de lois Gamma

## Stack

`Python` · `NumPy` · `SciPy` (`poisson`, `expon`, `gamma`) · `Matplotlib`
