# coding=utf-8


from paddle_game.utils.math import Line
from paddle_game.globals import Dimensions


class Ball:
    """Classe pour gérer les mouvements, les collisions et l'affichage de la balle."""
    def __init__(self):
        """Initialise une nouvelle balle."""
        self.r = 10  # attribut rayon
        self.vel = PVector(4, 4)  # attribut vitesse
        self.dir = PVector(1, -1)  # attribut direction
        self.pos = PVector(Dimensions.WIDTH / 2, Dimensions.HEIGHT / 2)  # attribut position

    def update(self):
        """Actualise la position de la balle."""
        # bord droit
        if self.pos.x > Dimensions.WIDTH - self.r and self.dir.x > 0:
            self.dir.x *= -1  # on change le signe de la direction
        # bord gauche
        if self.pos.x < self.r and self.dir.x < 0:
            self.dir.x *= -1
        # bord haut
        if self.pos.y < self.r and self.dir.y < 0:
            self.dir.y *= -1
        # bord bas
        if self.pos.y > Dimensions.HEIGHT - self.r and self.dir.y > 0:
            self.dir.y *= -1
        self.pos.x += self.vel.x * self.dir.x
        self.pos.y += self.vel.y * self.dir.y

    def draw(self):
        """Affiche la balle."""
        fill("#ffff64")
        noStroke()
        ellipse(self.pos.x, self.pos.y, self.r * 2, self.r * 2)        

    def hit_bottom(self):
        """
        Méthode de detection de collision de la balle avec le bas de l'écran.
        Retourne True si le ballon est en collision et False si non.
        """
        if self.pos.y + self.r > Dimensions.HEIGHT:
            return True
        return False

    def collide_with_object(self, object):
        """
        Méthode de detection de collision de la balle avec un rectangle.
        Retourne True si une collision a eu lieu et False si non.

        object: Any - Objet avec les attributs pos.x, pos.y, w et h
        """
        if (
            self.pos.x + self.r >= object.pos.x
            and self.pos.x - self.r <= object.pos.x + object.w
            and self.pos.y + self.r >= object.pos.y
            and self.pos.y - self.r <= object.pos.y + object.h
        ):
            line_ball = Line(
                self.pos.x,
                self.pos.y,
                self.pos.x + self.dir.x * self.r,
                self.pos.y + self.dir.y * self.r,
            )
            line_obj_left = Line(
                object.pos.x,
                object.pos.y,
                object.pos.x,
                object.pos.y + object.h,
            )
            line_obj_right = Line(
                object.pos.x + object.w,
                object.pos.y,
                object.pos.x + object.w,
                object.pos.y + object.h,
            )
            if line_ball.intersects_with_line(line_obj_left) or line_ball.intersects_with_line(line_obj_right):
                self.dir.x *= -1
                return True
            else:
                self.dir.y *= -1
                return True
        return False
    
    def collide_with_paddle(self, paddle):
        """
        Méthode de detection de collision de la balle avec le paddle.
        Retourne True si une collision a eu lieu et False si non.

        paddle: Paddle - Objet paddle
        """
        if (
            self.pos.y < paddle.pos.y and
            self.pos.y > paddle.pos.y - self.r and
            self.pos.x > paddle.pos.x - self.r and
            self.pos.x < paddle.pos.x + paddle.w + self.r
        ):
            self.dir.y = -1
            return True
        return False


    
    def multiply_velocity(self, amt):
        """
        Multiplie la vélocité de la balle par un nombre.

        amt: Number - Nombre multiplié à la vélocité
        """
        self.vel.x *= amt
        self.vel.y *= amt
