# coding=utf-8


from paddle_game.globals import Dimensions


class Paddle:
    """Classe pour gérer les mouvements et affichage du paddle."""
    def __init__(self):
        """Initialise un nouveau paddle au centre bas de l'écran."""
        self.w = 120  # attribut longueur du paddle
        self.h = 15  # attribut largeur du paddle
        # la position du paddle avec un objet Pvector
        self.pos = PVector(Dimensions.WIDTH / 2 - self.w / 2, Dimensions.HEIGHT - 40)
        self.isMovingLeft = False  # booléen pour mouvement à gauche
        self.isMovingRight = False  # idem à droite
        self.stepSize = 15  # pas pour le déplacement

    def draw(self):
        """Affiche le paddle."""
        fill("#ff9664")  # couleur de remplissage
        noStroke()  # pas de "bord"
        # affichage du rectangle rect(x,y,longueur, largeur)
        rect(self.pos.x, self.pos.y, self.w, self.h)

    def update(self):
        """Actualise la position du paddle."""
        if self.isMovingLeft and self.pos.x >= 0:
            self.pos.x -= self.stepSize
        if self.isMovingRight and self.pos.x + self.w <= Dimensions.WIDTH:
            self.pos.x += self.stepSize

