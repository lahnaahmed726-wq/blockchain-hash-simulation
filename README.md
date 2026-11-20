# Simulation d'une blockchain : des blocs reliés par des hash

**Auteur :** Ahmed Lahna — Master FinTech, Université Cadi Ayyad (cours Blockchain, TP3)

## Question étudiée
Pourquoi est-il pratiquement impossible de modifier un ancien bloc d'une blockchain sans que tout le monde s'en aperçoive ?

## Démarche
J'ai écrit un petit programme Python (`blockchain_simulation.py`) qui :
1. crée une chaîne de blocs, chacun contenant ses données, l'empreinte (hash SHA-256) du bloc précédent et un `nonce` ;
2. « mine » chaque bloc : il cherche un nonce pour que le hash commence par quatre zéros (preuve de travail simplifiée) ;
3. vérifie la validité de la chaîne ;
4. simule une fraude (modification d'une transaction passée) et montre que la chaîne devient invalide.

## Résultat
- La chaîne initiale est valide.
- Modifier le bloc 1 change son hash : la chaîne est détectée comme invalide.
- Même en recalculant le hash du bloc 1, le bloc 2 pointe toujours vers l'ancien hash : le lien est rompu. Il faudrait re-miner tous les blocs suivants.

Détails et explications dans [`rapport.md`](rapport.md).

## Utilisation
```
python blockchain_simulation.py
```
Python 3 suffit, aucune bibliothèque externe. Aucun argent réel n'est utilisé (les montants sont fictifs).

## Sources
- Bitcoin whitepaper, S. Nakamoto, 2008 : https://bitcoin.org/bitcoin.pdf
- Documentation Python `hashlib` : https://docs.python.org/3/library/hashlib.html
- Cours Blockchain, Pr. A. Elbasri, Master FinTech

## Outils utilisés
Python 3, GitHub Desktop, assistant IA (Claude, Anthropic) pour aider à écrire et tester le code et à structurer le rapport. J'ai relu et testé le code et je peux l'expliquer.
