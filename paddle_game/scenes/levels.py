# coding=utf-8


from paddle_game.game.level import create_level
from paddle_game.globals import Dimensions
from paddle_game.utils.add_brick import *

# Fichier pour définir la configuration de briques de chaque niveaux

def bricks_level1():
    """Génère la configuration de briques du niveau 1."""
    bricks = []
    for x in range(5, Dimensions.WIDTH - 80, 75):
        add_brick(bricks, x + 37.5, 65, 1)
    return bricks

def bricks_level2():
    """Génère la configuration de briques du niveau 2."""
    bricks = []
    brick_pos = 0
    for x in range(5, Dimensions.WIDTH - 80, 75):
        if brick_pos == 2:
            add_bad_brick(
                bricks, x + 37.5, 65
            )
        elif brick_pos == 4:
            add_good_brick(
                bricks, x + 37.5, 65
            )
        else:
            add_brick(bricks, x + 37.5, 65, 1)
        add_brick(bricks, x + 37.5, 100, 1)
        brick_pos += 1
    return bricks

def bricks_level3():
    """Génère la configuration de briques du niveau 3."""
    bricks = []
    brick_pos = 0
    for x in range(5, Dimensions.WIDTH - 80, 75):
        if brick_pos == 5:
            add_bad_brick(
                bricks, x + 37.5, 65
            )
        elif brick_pos == 1:
            add_good_brick(
                bricks, x + 37.5, 65
            )
        else:
            add_brick(bricks, x + 37.5, 65, 2)
        add_brick(bricks, x + 37.5, 100, 1)
        brick_pos += 1
    return bricks

def bricks_level4():
    """Génère la configuration de briques du niveau 4."""
    bricks = []
    brick_pos = 0
    for x in range(5, Dimensions.WIDTH - 80, 75):
        if brick_pos == 3:
            add_bad_brick(
                bricks, x + 37.5, 65
            )
        else:
            add_brick(bricks, x + 37.5, 65, 2)
        if brick_pos == 4:
            add_good_brick(
                bricks, x + 37.5, 100
            )
        else:
            add_brick(bricks, x + 37.5, 100, 1)
        add_brick(bricks, x + 37.5, 135, 1)
        brick_pos += 1
    return bricks

def bricks_level5():
    """Génère la configuration de briques du niveau 5."""
    bricks = []
    brick_pos = 0
    for x in range(5, Dimensions.WIDTH - 80, 75):
        if brick_pos == 0:
            add_bad_brick(
                bricks, x + 37.5, 65
            )
        else:
            add_brick(bricks, x + 37.5, 65, 2)
        if brick_pos == 6:
            add_good_brick(
                bricks, x + 37.5, 100
            )
        else:
            add_brick(bricks, x + 37.5, 100, 2)
        brick_pos += 1
    return bricks

def bricks_level6():
    """Génère la configuration de briques du niveau 6."""
    bricks = []
    brick_pos = 0
    for x in range(5, Dimensions.WIDTH - 80, 75):
        if brick_pos == 0:
            add_bad_brick(
                bricks, x + 37.5, 65
            )
        else:
            add_brick(bricks, x + 37.5, 65, 2)
        if brick_pos == 6:
            add_good_brick(
                bricks, x + 37.5, 100
            )
        else:
            add_brick(bricks, x + 37.5, 100, 2)
        brick_pos += 1
    return bricks

def bricks_level7():
    """Génère la configuration de briques du niveau 7."""
    bricks = []
    brick_pos = 0
    for x in range(5, Dimensions.WIDTH - 80, 75):
        if brick_pos == 0:
            add_bad_brick(
                bricks, x + 37.5, 65
            )
        elif brick_pos == 4:
            add_good_brick(
                bricks, x + 37.5, 65
            )
        else:
            add_brick(bricks, x + 37.5, 65, 2)
        if brick_pos == 2 or brick_pos == 3:
            add_unbreakable_brick(
                bricks, x + 37.5, 100
            )
        else:
            add_brick(bricks, x + 37.5, 100, 2)
        brick_pos += 1
    return bricks

# Générer les scènes à partir des configurations
Level1 = create_level(1, bricks_level1())
Level2 = create_level(2, bricks_level2())
Level3 = create_level(3, bricks_level3())
Level4 = create_level(4, bricks_level4())
Level5 = create_level(5, bricks_level5())
Level6 = create_level(6, bricks_level6())
Level7 = create_level(7, bricks_level7())