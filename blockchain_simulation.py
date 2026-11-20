"""Simulation pédagogique d'une blockchain : des blocs reliés par des hash SHA-256.
Aucun argent réel, aucune connexion réseau. Usage : python blockchain_simulation.py
"""
import hashlib
import json
import time

DIFFICULTE = 4  # le hash doit commencer par 4 zéros (preuve de travail simplifiée)


def calculer_hash(index, horodatage, donnees, hash_precedent, nonce):
    contenu = json.dumps(
        [index, horodatage, donnees, hash_precedent, nonce], sort_keys=True
    )
    return hashlib.sha256(contenu.encode()).hexdigest()


class Bloc:
    def __init__(self, index, donnees, hash_precedent):
        self.index = index
        self.horodatage = time.time()
        self.donnees = donnees
        self.hash_precedent = hash_precedent
        self.nonce = 0
        self.hash = self.miner()

    def miner(self):
        """Cherche un nonce tel que le hash commence par DIFFICULTE zéros."""
        while True:
            h = calculer_hash(self.index, self.horodatage, self.donnees,
                              self.hash_precedent, self.nonce)
            if h.startswith("0" * DIFFICULTE):
                return h
            self.nonce += 1


class Chaine:
    def __init__(self):
        self.blocs = [Bloc(0, "Bloc de genèse", "0" * 64)]

    def ajouter(self, donnees):
        precedent = self.blocs[-1]
        self.blocs.append(Bloc(len(self.blocs), donnees, precedent.hash))

    def est_valide(self):
        for i, bloc in enumerate(self.blocs):
            recalcul = calculer_hash(bloc.index, bloc.horodatage, bloc.donnees,
                                     bloc.hash_precedent, bloc.nonce)
            if recalcul != bloc.hash or not bloc.hash.startswith("0" * DIFFICULTE):
                return False, f"Bloc {i} : son contenu ne correspond plus à son hash"
            if i > 0 and bloc.hash_precedent != self.blocs[i - 1].hash:
                return False, f"Bloc {i} : le lien avec le bloc {i - 1} est rompu"
        return True, "Chaîne valide"

    def afficher(self):
        for b in self.blocs:
            print(f"Bloc {b.index} | données : {b.donnees}")
            print(f"  hash précédent : {b.hash_precedent[:16]}...")
            print(f"  hash           : {b.hash[:16]}...  (nonce = {b.nonce})")


if __name__ == "__main__":
    chaine = Chaine()
    chaine.ajouter("Alice envoie 2 TBTC à Bob")
    chaine.ajouter("Bob envoie 1 TBTC à Sara")
    chaine.ajouter("Sara envoie 0.5 TBTC à Alice")

    print("=== Chaîne initiale ===")
    chaine.afficher()
    print(chaine.est_valide()[1])

    print("\n=== Tentative de fraude : on modifie le bloc 1 ===")
    chaine.blocs[1].donnees = "Alice envoie 200 TBTC à Bob"
    print(chaine.est_valide()[1])

    print("\n=== Même après recalcul du hash du bloc 1 (sans re-miner la suite) ===")
    b = chaine.blocs[1]
    b.nonce = 0
    b.hash = b.miner()
    print(chaine.est_valide()[1])
