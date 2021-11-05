# coding=utf-8


class Brick:
    """Classe pour gérer la position, les coups et l'affichage des briques."""
    # attribut de classe: un dictionnaire de couleurs
    COLORS = {1: "#64ff96", 2: "#ff6496", 3: "#9664ff"}

    def __init__(self, x, y, hits, good=False, bad=False, unbreakable=False, color=None):  # le constructeur
        """
        Initialise une nouvelle brique.

        x: Number - Coordonnée X de la brique à ajouter
        y: Number - Coordonnée Y de la brique à ajouter
        hits: Number - Nombre de coups que peut prendre la brique avant de casser
        good: Boolean - (Optionnel) Si la brique est un bonus ou pas
        bad: Boolean - (Optionnel) Si la brique est un malus ou pas
        unbreakable: Boolean - (Optionnel) Si la brique est incassable
        color: String - (Optionnel) Couleur de la brique
        """
        self.w = 75  # attribut longueur
        self.h = 20  # attribut largeur
        self.pos = PVector(x, y)  # attribut position
        self.hits = hits  # attribut clé pour la couleur
        self.good = good
        self.bad = bad
        self.unbreakable = unbreakable
        self.color = color
        self.dead = False
    
    def hit(self):
        """
        Donne un coup à la brique. Si la brique n'a plus de vie, l'attribut
        dead changera à True.
        """
        if not self.unbreakable:
            if self.hits > 0:
                self.hits -= 1
            if self.hits == 0:
                self.dead = True

    def draw(self):
        """Affiche la brique."""
        color = None
        if self.color:
            color = self.color
        else:
            color = Brick.COLORS.get(min(self.hits, 3), "#000000")
        fill(color)
        stroke("#ffffff")  # couleur du bord
        strokeWeight(2)  # épaisseur des bords
        rect(self.pos.x, self.pos.y, self.w, self.h)
