# coding=utf-8


from paddle_game.globals import Dimensions


class Scoreboard:
    """Classe pour gérer les vies du joueur et de son score."""
    def __init__(self, initial_score=0, lives=3):
        """
        Initialise un nouveau scoreboard.

        initial_score: Number - (Optionnel) Score de base du scoreboard
        lives: Number - (Optionnel) Nombre de vies du joueur
        """
        self.score = initial_score
        self.lives = lives
        self.h = 30
        self.w = 60
        self.margin = 10
        self.padding = 5
        self.pos = PVector(Dimensions.WIDTH - self.w - self.margin, self.margin)
        self.heart = loadImage("assets/heart.png")

    def draw(self):
        """Affiche le nombre de vies en haut à gauche et le score en haut à droite."""
        textSize(self.h * 1.5 - self.padding * 3)
        fill("#ffffff")  # couleur de remplissage
        text(self.score, self.pos.x + self.padding, self.pos.y + self.h - self.padding)
        for x in range(self.lives):
            image(self.heart, self.margin + x * 37, self.margin)

    def increment(self, step=1):
        """
        Incrémente le score par step.

        step: Number - Nombre de points à incrémenter
        """
        self.score += step

    def decrement(self, step=-1):
        """
        Décrémente le score par step.

        step: Number - Nombre de points à décrémenter
        """
        self.score -= step

    def has_lost(self):
        """
        Detecte si le joueur à perdu ou non.
        Retourne True si le joueur n'a plus de vies.
        """
        if self.lives <= 0:
            return True
        return False
    
    def set_lives(self, new_lives):
        """
        Changer le nombres de vies à une nouvelle valeur.

        new_lives: Number - Nouveau nombre de vies
        """
        self.lives = new_lives

    def add_life(self, step=1):
        """Ajouter une vie au joueur."""
        self.lives += step

    def loose_life(self, step=1):
        """Enlever une vie au joueur."""
        self.lives -= step
