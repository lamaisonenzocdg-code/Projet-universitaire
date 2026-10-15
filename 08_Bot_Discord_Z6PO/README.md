# BOT-MK — Z6PO_ · Mandalore Ka'rta

Bot Discord de la communauté **Mandalore Ka'rta** (Clash of Clans, FR).  
Gestion des joueurs, guerres, rosters de ligue, esport et calendrier — avec une API REST interne qui alimente le [site esport](https://mk-esport.netlify.app/).

---

## Stack

| Composant | Technologie |
|---|---|
| Runtime | Node.js |
| Discord | discord.js v14 |
| CoC API | clashofclans.js |
| Base de données | MongoDB Atlas |
| Rendu image | canvas |
| Serveur API | Express + CORS |
| Hébergement | Oracle Cloud Free Tier (Ubuntu 22.04) |
| Process manager | PM2 |
| Déploiement | GitHub → `~/update-bot.sh` |

---

## Commandes slash

### Joueurs & comptes CoC

| Commande | Description |
|---|---|
| `/lier-joueur` | Associe un tag CoC à un membre Discord |
| `/supprimer-joueur` | Supprime la liaison CoC d'un membre |
| `/supprimer-compte-tag` | Délie un tag CoC précis |
| `/joueurs-lies` | Liste tous les joueurs liés du serveur |
| `/mes-comptes` | Affiche les comptes CoC d'un membre |
| `/profil-joueur` | Profil complet d'un joueur (HDV, trophées, ligue…) |
| `/stats-joueur` | Stats de guerre d'un joueur |

### Clans

| Commande | Description |
|---|---|
| `/lier-clan` | Enregistre un clan (nom court + tag CoC) |
| `/supprimer-clan` | Supprime un clan enregistré |
| `/clans-enregistres` | Liste les clans enregistrés |
| `/clan` | Infos générales d'un clan |
| `/membres` | Liste des membres d'un clan avec HDV et trophées |
| `/guerre` | Statut de la guerre en cours d'un clan |
| `/discord-links` | Correspondances Discord ↔ CoC pour un clan |

### Rappels de guerre (GDC)

| Commande | Description |
|---|---|
| `/rappel` | Envoie un rappel pour la guerre d'un clan |
| `/rappel-tous` | Rappels pour tous les clans configurés |
| `/rappel-all` | Rappel global (tous clans, tous membres) |
| `/rappel-auto` | Active / désactive les rappels automatiques |
| `/configurer-salon` | Définit le salon cible pour les rappels |

### Roster de Ligue de Clans (LDC)

| Commande | Description |
|---|---|
| `/roster-creer` | Crée un roster pour un clan (filtre HDV optionnel) |
| `/roster-poster` | Poste le roster en mode `signup` (inscriptions) ou `post` (publication) |
| `/roster-ajouter` | Ajoute un joueur au roster |
| `/roster-retirer` | Retire un joueur du roster |
| `/roster-deplacer` | Déplace un compte d'un roster vers un autre |
| `/roster-role` | Attribue un rôle Discord aux inscrits |
| `/roster-fin-ligue` | Archive le roster de fin de saison |
| `/roster-supprimer` | Supprime un roster |
| `/roster-vider` | Vide un roster sans le supprimer |
| `/ligue-inscrits` | Liste les inscrits LDC d'un clan |

### Esport

| Commande | Description |
|---|---|
| `/esport effectif` | Affiche l'effectif esport (Elite ou Death Watch) |
| `/esport joueur-ajouter` | Ajoute un joueur à l'effectif esport |
| `/esport joueur-retirer` | Retire un joueur de l'effectif esport |
| `/esport actualiser` | Synchronise les données HDV depuis CoC |
| `/esport calendrier` | Configure / déclenche l'envoi du calendrier hebdo |

---

## Automatisations planifiées

| Heure (Paris) | Action |
|---|---|
| **08:00** chaque matin | Envoi du calendrier esport de la semaine dans le salon configuré |
| Sync HDV | Mise à jour quotidienne des niveaux HDV des joueurs esport depuis l'API CoC |

Le calendrier hebdomadaire est posté sous forme d'embed Discord avec :
- La liste des matchs de la semaine (équipe, adversaire, date, heure)
- Un bilan victoires / défaites
- Un bouton **"Voir le calendrier complet"** → [mk-esport.netlify.app](https://mk-esport.netlify.app/)

---

## API REST interne (port 3000)

Utilisée par le site esport. Toutes les routes renvoient du JSON.

| Méthode | Route | Description |
|---|---|---|
| `GET` | `/esport/joueurs` | Liste tous les joueurs esport (id normalisé = tag CoC) |
| `GET` | `/esport/matchs` | Liste tous les matchs |
| `POST` | `/esport/matchs` | Crée ou met à jour un match |
| `DELETE` | `/esport/matchs/:id` | Supprime un match |
| `GET` | `/esport/compets` | Liste les compétitions |
| `POST` | `/esport/compets` | Crée ou met à jour une compétition |
| `DELETE` | `/esport/compets/:id` | Supprime une compétition |

### Schéma MongoDB

**`esport_joueurs`**
```js
{
  tag,        // "#ABC123" — clé primaire, tag CoC
  discord,    // pseudo Discord
  discordId,
  hdv,        // "HDV 18" (string)
  hdvNum,     // 18 (entier)
  cocName,
  updatedAt
}
```

**`esport_matchs`**
```js
{
  id,         // identifiant personnalisé
  team,       // "elite" | "dw"
  comp,       // nom de la compétition liée
  title,
  date, time,
  squad,      // effectif minimum
  prep,       // temps de préparation (min)
  war,        // durée de guerre (min)
  timed,      // boolean — attaques timées
  players,    // [tag, tag, ...]
  result,     // "tbd" | "win" | "loss"
  su, st,     // étoiles nous / étoiles adversaire
  notes
}
```

**`esport_compets`**
```js
{
  name,       // nom de la compétition
  team,       // "elite" | "dw"
  status,     // "active" | "finished"
  rounds      // tableau de phases / résultats
}
```

---

## Site esport — mk_esport.html

Fichier unique déployé sur [Netlify](https://mk-esport.netlify.app/).

**Fonctionnalités :**
- Calendrier hebdomadaire (navigation semaine par semaine)
- Fiche match : sélection des joueurs, résultat, notes
- Badge compétition ⚔ sur les cartes de match si une compétition est active
- Page Compétitions : bilan W/L, barre de progression des phases, prochain match lié, joueurs engagés
- Page Joueurs : effectif avec badges HDV colorés (orange = Élite, teal = Death Watch)
- Accès protégé par mot de passe (mode édition / mode lecture seule)
- **Responsive mobile** : sidebar en overlay avec bouton hamburger ☰, calendrier en liste verticale, modals plein écran

---

## Variables d'environnement

| Variable | Description |
|---|---|
| `DISCORD_TOKEN` | Token du bot Discord |
| `CLIENT_ID` | Application ID Discord |
| `COC_EMAIL` | Email du compte développeur CoC |
| `COC_PASSWORD` | Mot de passe CoC |
| `MONGODB_URI` | URI de connexion MongoDB Atlas |

---

## Emojis serveur

Le bot utilise des emojis custom (TH10–TH18, clans, utilitaires) définis dans `EMOJI_IDS` et `CLAN_EMOJIS` en haut de `bot.js`.  
Pour retrouver un ID : tape `\:nom_emoji:` dans Discord.

---

## Notes techniques

- Les `_id` MongoDB (ObjectId) sont normalisés côté API : l'endpoint `/esport/joueurs` retourne `id = tag CoC` pour éviter les bugs d'identification côté front-end.
- Les embeds Discord sont limités à **1024 caractères par champ** — les longs messages sont découpés (~8 lignes max).
- Les backticks dans les template literals JS sont un piège fréquent — vérifier l'échappement.
- Le bot principal et un bot esport dédié coexistent sur le serveur esport — ne pas les fusionner.
