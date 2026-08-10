# Finance Quantitative — VaR & modélisation ARMA-GARCH

**Cours :** Introduction à la VaR — Master 2 IREF, Université de Bordeaux
**Actif étudié :** Grupo Financiero Banorte (GBOOF, Mexique)

## Contenu

### Projet 1 — `Projet1_VaR_Banorte.pdf`
Analyse des caractéristiques statistiques des rendements logarithmiques du titre, et calcul de la Value-at-Risk par plusieurs approches (paramétrique, historique).

### Projet 2 — `Projet2_ARMA_GARCH_Banorte.pdf`
Suite du projet 1 : modélisation de la série des rendements par un processus **ARMA-GARCH(1,1)** avec distribution asymétrique, justifiée par la forte leptokurticité (queues épaisses, kurtosis > 3) et l'asymétrie modérée des rendements observés. Prévision de la VaR conditionnelle et backtesting.

### `import_donnees_marche.R`
Script R de récupération automatisée des cours boursiers (via `yfR`) et d'export structuré vers Excel — utilisé pour préparer les données AAPL / S&P 500 des cas pratiques.

### `AAPL_GSPC_donnees.xlsx`
Données de cours quotidiens AAPL et S&P 500 utilisées pour les cas pratiques associés.

## Stack

`R` (`yfR`, `dplyr`, `writexl`) · économétrie financière (ARMA-GARCH) · Value-at-Risk · backtesting
