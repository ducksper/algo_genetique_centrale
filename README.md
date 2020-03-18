![Graphique obtenue pour PI = générer_PI(100, 100), m = 10, proba = 0.2, g = 10000](./algo.png)

# Mission d'exploration martienne

Le projet présenté est basé sur le sujet Informatique du **concours Centrale-Supélec** (MP, PC, PSI, TSI) de 2017. L'objectif du projet est de mettre en oeuvre l'**algorithme génétique** présenté dans la partie III du sujet; pour cette raison la partie II n'est que peu abordée. 

L'algorithme est écrit en langage Python 3.6.8. Les modules utilisés sont: 
- math,
- numpy (restriction sujet),
- random,
- inspect (pour débugger, non important),
- matplotlib.pyplot (affichage graphique, optionnel mais vivement conseillé).

Pour comprendre au mieux l'algorithme je conseille de lire au moins l'énoncé du sujet puis d'analyser le script. 

## Principe d'un algorithme génétique

(wikipédia + sujet)
Les **algorithmes génétiques** appartiennent à la famille des algorithmes évolutionnistes (s'inspirant de la théorie de l'évolution). Leur but est d'obtenir une solution approchée à un problème d'optimisation, lorsqu'il n'existe pas de méthode exacte (ou que la solution est inconnue) pour le résoudre en un temps raisonnable. Les algorithmes génétiques utilisent la notion de sélection naturelle et l'appliquent à une population de solutions potentielles au problème donné. La solution est approchée par « bonds » successifs.

Les algorithmes génétiques font intervenir cinq traitements.

- **Initialisation:**
Il s’agit de créer une population d’origine composée de 𝑚 individus (ici des chemins pour l’exploration à planifier). Généralement la population de départ est produite aléatoirement.

- **Évaluation:**
Cette étape consiste à attribuer à chaque individu de la population courante une note correspondant à sa capacité à répondre au problème posé. Ici la note sera simplement la longueur du chemin.

- **Sélection:**
Une fois tous les individus évalués, l’algorithme ne conserve que les « meilleurs » individus. Plusieurs méthodes de sélection sont possibles : choix aléatoire, ceux qui ont obtenu la meilleure note, élimination par tournoi, etc.

- **Croisement:**
Les individus sélectionnés sont croisés deux à deux pour produire de nouveaux individus et donc une nouvelle population. La fonction de croisement (ou reproduction) dépend de la nature des individus.

- **Mutation:**
Une proportion d’individus est choisie (généralement aléatoirement) pour subir une mutation, c’est-à-dire une transformation aléatoire. Cette étape permet d’éviter à l’algorithme de rester bloqué sur un optimum local. En répétant les étapes de sélection, croisement et mutation, l’algorithme fait ainsi évoluer la population, jusqu’à trouver un individu qui réponde au problème initial. Cependant dans les cas pratiques d’utilisation des algorithmes génétiques, il n’est pas possible de savoir simplement si le problème est résolu (le plus court chemin figure-t-il dans ma population ?). On utilise donc des conditions d’arrêt heuristiques basées sur un critère arbitraire.
