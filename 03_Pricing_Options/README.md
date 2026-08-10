# Pricing d'options — Black-Scholes & Monte-Carlo

## `Pricer_BlackScholes_Greeks.xlsm`
Pricer d'options européennes développé sous Excel/VBA à partir du modèle de **Black-Scholes**, avec :
- feuille de calcul du prix de l'option (`Pricer_BS`)
- feuille de calcul des **Greeks** (Delta, Gamma, Vega, Theta, Rho)
- gestion des dividendes (`Dividend`)
- plages nommées pour les paramètres du modèle (`S0`, `K`, `sigma`, `T`, `RiskFree`, `r_D1`, `r_D2`, `r_Nd1`, `r_Nd2`...)

⚠️ Le fichier contient une macro VBA (`vbaProject`) — Excel proposera d'activer les macros à l'ouverture.

## `Monte_Carlo_Pricing_Options.ipynb`
Notebook pédagogique et pratique sur la **simulation de Monte-Carlo** appliquée à la valorisation d'options :
- principe et contexte de la méthode
- modélisation du sous-jacent par **Mouvement Brownien Géométrique (GBM)**
- génération des trajectoires de prix, calcul du payoff, actualisation
- implémentation Python complète et interprétation des résultats

## Stack

`VBA` · `Excel` · `Python` (`NumPy`, notebook Jupyter) · modèle de Black-Scholes · simulation de Monte-Carlo
