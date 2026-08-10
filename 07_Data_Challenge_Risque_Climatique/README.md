# Data Challenge — Évaluation des risques climatiques physiques

**Contexte :** Data Challenge proposé par la **Caisse des Dépôts** dans le cadre du cours "Finance et risques climatiques" — Master 2 IREF, 2025-2026
**Équipe (Groupe 4) :** Enzo Lamaison, Fanis Mador, Corentin Ané

## Objectif

Développer une **méthodologie générique et transposable** pour évaluer l'exposition climatique physique de tout portefeuille d'actifs localisés en France, à partir de données institutionnelles ouvertes uniquement (DRIAS/Météo-France, Géorisques, IGN, Copernicus).

## Démarche

Le risque physique est décomposé en trois dimensions classiques (aléa, exposition, vulnérabilité), combinées de façon opérationnelle :

1. **Sélection des indicateurs par aléa** — sécheresse (SWI + jours sans pluie, avec un focus sur le risque de Retrait-Gonflement des Argiles), inondations (zonage TRI + précipitations extrêmes), feux de forêt (IFM + couverture forestière), vagues de chaleur (jours à Tx > 35°C)
2. **Construction des scores d'aléa communaux** — agrégation spatiale des données DRIAS à l'échelle communale, normalisation par quantile-rank à l'échelle nationale, reclassement en 5 niveaux de risque
3. **Ajustement au niveau de l'actif** — héritage du score communal, pondération par la vulnérabilité sectorielle (nomenclature NACE), correction selon la maturité de l'actif (coefficient de 0,8 à 1,2)
4. **Analyse au niveau du portefeuille** — scores moyens et pondérés par les encours, part de l'encours en risque élevé (niveaux 4-5), comparaison entre trois portefeuilles types

**Scénario climatique retenu :** DRIAS RCP 4.5, horizon 2041-2070 (scénario intermédiaire, cohérent avec des actifs de maturité moyenne à longue).

## Résultats clés

La comparaison de trois portefeuilles types fait ressortir des profils de risque contrastés : exposition dominante aux inondations et aux vagues de chaleur pour le premier, profil diversifié et modéré pour le second, exposition plus marquée aux risques climatiques futurs (feux de forêt, chaleur) pour le troisième — illustrant la capacité de la méthodologie à hiérarchiser et discriminer des portefeuilles entre eux.

## Limites et perspectives identifiées

- Les scores obtenus sont relatifs (échelle 1-5) et ne traduisent pas directement une perte financière
- La vulnérabilité sectorielle repose sur une grille encore simplifiée
- Prolongements envisagés : fonctions de dommages financiers, aléas supplémentaires, automatisation Python du pipeline

## Fichiers

- `Rapport_Methodologie_Risque_Climatique.docx` — rapport méthodologique complet
- `Presentation_Data_Challenge.pdf` — support de présentation du projet (cartographie, tableaux de scores, comparaison des portefeuilles)

## Stack

`QGIS` (agrégation spatiale et jointures cartographiques) · sources de données ouvertes (DRIAS, Géorisques, IGN, Copernicus/CORINE Land Cover) · construction d'indicateurs de risque · analyse de portefeuille
