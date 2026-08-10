# Analyse de Portefeuille & Backtesting

## `Etude_Cas_Amazon_LigueUn.pdf`
**Co-auteur :** Marco Douet
Étude de cas en choix d'investissement : évaluation de la rentabilité du renouvellement des droits de retransmission de la Ligue 1 par Amazon Prime Video (2026–2030, ~200 M€/an), à partir de données de marché (Yahoo Finance) et dans une optique d'analyste en fonds d'investissement spécialisé médias.

## Backtesting de stratégie de portefeuille

Ensemble de données et résultats issus d'un projet de construction et de backtesting d'une stratégie de portefeuille actions (univers de titres italiens — Milan, `.MI`) :

| Fichier | Contenu |
|---|---|
| `synthetic_prices_full.csv` | Historique de prix (42 actifs) utilisé pour la construction du portefeuille |
| `selected_tickers.csv` | Liste des titres retenus dans l'univers d'investissement |
| `weights_backtest.csv` | Poids alloués à chaque actif au cours du temps |
| `strategy_phase_A.csv` | Résultats de la première phase de la stratégie |
| `cumulative_returns_backtest.csv` / `cumulative_returns_strategy_bt_new.csv` | Rendements cumulés de la stratégie testée |
| `cumulative_returns_strategy_bt_new.png` / `cumulative_returns_benchmarking_bt_new.png` | Visualisations des performances vs. benchmark |
| `portefeuilles.csv` | Journal des opérations (achats/ventes) d'un portefeuille suivi |

## Stack

`Python` (analyse de données, backtesting) · gestion de portefeuille · analyse de la performance
