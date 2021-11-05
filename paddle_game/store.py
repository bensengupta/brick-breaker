# coding=utf-8


class Store():
    """
    Classe pour servir de database au jeu. Toute les scènes peuvent écrire et lire du store
    on peut donc transmettre des variables d'une scène à un autre sans passer par des
    paramètres de navigation.
    """
    def __init__(self):
        """Initialise un nouveau store."""
        # Initialise le store avec des valeurs prédéfinis
        self.data = {
            'highest_level': 1,
            'current_level': 1,
        }
    
    def update(self, key, val):
        """
        Ajoute/met à jour un élément du store en associant une clée key à une valeur val.

        key: String
        val: Any
        """
        self.data[key] = val
    
    def get(self, key):
        """
        Cherche un élément du store par sa clée key
        Retourne None si la clée n'existe pas dans le store.

        key: String
        """
        return self.data.get(key, None)
