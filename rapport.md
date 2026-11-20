# Rapport : comment les hash protègent l'historique d'une blockchain

## 1. Idée générale
Une blockchain est une suite de blocs. Chaque bloc contient une empreinte (hash) du bloc précédent. Si on change une seule lettre dans un ancien bloc, son hash change complètement, et tous les blocs suivants deviennent incohérents.

## 2. Les trois notions utilisées
| Notion | Rôle dans le programme |
|---|---|
| **Hash SHA-256** | Empreinte de 64 caractères d'un bloc. Un changement minime des données donne un hash totalement différent. |
| **Chaînage** | Le champ `hash_precedent` de chaque bloc relie ce bloc au précédent. |
| **Preuve de travail (nonce)** | Pour être accepté, le hash doit commencer par `0000`. Il faut essayer de nombreux nonces : miner coûte du calcul. |

## 3. Résultats de l'exécution
| Bloc | Données | Nonce trouvé |
|---|---|---|
| 0 | Bloc de genèse | 6 338 |
| 1 | Alice envoie 2 TBTC à Bob | 32 760 |
| 2 | Bob envoie 1 TBTC à Sara | 3 750 |
| 3 | Sara envoie 0.5 TBTC à Alice | 176 224 |

(Les nonces changent à chaque exécution, car l'horodatage fait partie du hash.)

**Test de fraude :**
1. On modifie « 2 TBTC » en « 200 TBTC » dans le bloc 1 → le programme répond : *le contenu du bloc 1 ne correspond plus à son hash*.
2. L'attaquant recalcule le hash du bloc 1 → le programme répond : *le bloc 2 pointe vers l'ancien hash, le lien est rompu*.
3. Pour réussir, l'attaquant devrait re-miner le bloc 1, puis les blocs 2 et 3, plus vite que le reste du réseau.

## 4. Lien avec Bitcoin (et TestNet4)
Bitcoin fonctionne selon le même principe : chaque en-tête de bloc contient le hash du bloc précédent, et la preuve de travail impose un hash sous une cible de difficulté. TestNet4 est un réseau de test qui utilise le même mécanisme, avec des coins sans valeur.

## 5. Limites de la simulation
- Un seul ordinateur : pas de réseau de nœuds ni de consensus entre plusieurs copies de la chaîne.
- Difficulté fixe et très faible (4 zéros), alors que Bitcoin ajuste la difficulté et demande une puissance énorme.
- Pas de signatures numériques, pas de transactions UTXO : les données sont du simple texte.

## 6. Conclusion
L'immuabilité d'une blockchain ne vient pas d'un interdit technique de modifier, mais du coût : modifier le passé oblige à refaire tout le travail des blocs suivants, et les autres nœuds rejettent la chaîne falsifiée.

## 7. Sources et outils
Voir le README. Code écrit et testé avec l'aide d'un assistant IA (Claude), relu et compris par l'auteur.
