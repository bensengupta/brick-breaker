# coding=utf-8


from paddle_game.game.brick import Brick


def add_brick(bricks, x, y, hits):
    """
    Ajoute une nouvelle brique à une liste de briques.

    bricks: Brick[] - Liste de briques à lequel il faut ajouter des briques
    x: Number - Coordonnée X de la brique à ajouter
    y: Number - Coordonnée Y de la brique à ajouter
    hits: Number - Nombre de coups que peut prendre la brique avant de casser
    """
    bricks.append(Brick(x, y, hits))

def add_good_brick(bricks, x, y):
    """
    Ajoute une nouvelle brique bonus à une liste de briques.

    bricks: Brick[] - Liste de briques à lequel il faut ajouter des briques
    x: Number - Coordonnée X de la brique à ajouter
    y: Number - Coordonnée Y de la brique à ajouter
    """
    bricks.append(Brick(x, y, 1, good=True, color='#00ff00'))

def add_bad_brick(bricks, x, y):
    """
    Ajoute une nouvelle brique malus à une liste de briques.

    bricks: Brick[] - Liste de briques à lequel il faut ajouter des briques
    x: Number - Coordonnée X de la brique à ajouter
    y: Number - Coordonnée Y de la brique à ajouter
    """
    bricks.append(Brick(x, y, 1, bad=True, color='#ff0000'))

def add_unbreakable_brick(bricks, x, y):
    """
    Ajoute une nouvelle brique incassable à une liste de briques.

    bricks: Brick[] - Liste de briques à lequel il faut ajouter des briques
    x: Number - Coordonnée X de la brique à ajouter
    y: Number - Coordonnée Y de la brique à ajouter
    """
    bricks.append(Brick(x, y, 1, unbreakable=True, color='#5d6169'))