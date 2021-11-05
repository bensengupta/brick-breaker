# coding=utf-8


from copy import deepcopy
from paddle_game.globals import Dimensions
from paddle_game.event import Event
from random import randint

from paddle_game.game.ball import Ball
from paddle_game.game.paddle import Paddle
from paddle_game.game.scoreboard import Scoreboard
from paddle_game.scene import Scene


def create_level(level_number, initial_bricks):
    """
    Génère un nouvelle scène pour un nouveau niveau.

    level_number: Number - Numéro de niveau
    initial_bricks: Brick[] - Liste de briques du niveau
    """
    class Level(Scene):
        def __init__(self, *scene_params):
            """
            Initialise une nouvelle scène de niveau.

            *scene_params: Any - Paramètres de scène à passer au constructeur de Scene
            """
            super(Level, self).__init__(*scene_params)
            self.next_level_name = "level{}".format(level_number + 1)
            self.level = level_number
            self.sb = Scoreboard()
            self.reset() # réinialise le niveau
            # ajoute les event handler à la liste d'event handler
            self.add_event_handler(Event.KEYUP, self.on_keyup)
            self.add_event_handler(Event.KEYDOWN, self.on_keydown)

        def reset(self):
            """Methode appelé quand une autre scène veut réinitialiser celle-ci."""
            self.sb.set_lives(3)
            self.playing_game = True
            self.level_score = 0
            self.paddle = Paddle()
            self.bricks = deepcopy(initial_bricks)
            self.balls = [Ball()]
            self.ready_to_toggle_pause = True

        def apply_bonus(self):
            """
            Methode appelé quand un bonus est touché.
            Choisi une action aléatoirement.
            """
            choice = randint(0, 1)
            if choice == 0:
                self.paddle.w += 30 # ajoute 30 de largeur au paddle
            elif choice == 1:
                self.sb.add_life() # ajoute une vie
        
        def apply_malus(self):
            """
            Methode appelé quand un malus est touché.
            Choisi une action aléatoirement.
            """
            choice = randint(0, 1)
            if choice == 0:
                self.balls.append(Ball()) # ajoute une balle au niveau
            elif choice == 1:
                for ball in self.balls:
                    ball.multiply_velocity(1.5) # augmente la vitesse des ballons par 50%

        def freeze(self):
            """
            Méthode pour pauser le niveau.
            """
            print('Level: Froze game')
            self.playing_game = False

        def unfreeze(self):
            """
            Méthode pour resumer le niveau après un Level.freeze().
            """
            print('Level: Unfroze game')
            self.playing_game = True

        def draw(self):
            """Affiche le niveau."""
            background(0, 0, 0)
            textSize(40)
            fill("#303030")
            text("Niveau {}".format(self.level), Dimensions.WIDTH / 2.6, Dimensions.HEIGHT / 1.9)
            self.sb.draw()
            self.paddle.draw()
            for ball in self.balls:
                ball.draw()
            if self.playing_game:
                self.paddle.update()
                for ball in self.balls:
                    ball.update()
                for ball in self.balls:
                    if ball.hit_bottom():
                        # Balle touche le bas de l'écran = joueur perd une vie
                        self.sb.loose_life()
                        if self.sb.has_lost():
                            # Plus de vies = joueur perd le niveau
                            self.store.update('current_level', self.level + 1)
                            self.show_overlay('level_end', self.level, False, self.sb.score)
                # Initialise la variable has_won à True
                has_won = True
                if not self.bricks == []:
                    for brick in self.bricks:
                        # Dès qu'on détecte une brique normal, qui n'est ni spéciale, ni incassable
                        # on sait qu'on doit continuer a jouer pour tous les casser
                        if not brick.good and not brick.bad and not brick.unbreakable:
                            has_won = False
                            break
                if has_won:
                    # Plus de briques = joueur gagne le niveau
                    self.store.update('current_level', self.level + 1)
                    # Augmente le niveau maximal atteint
                    self.store.update(
                        'highest_level',
                        max(
                            self.store.get('highest_level'),
                            self.level + 1
                        )
                    )
                    # Montrer l'overlay de fin de niveau
                    self.show_overlay('level_end', self.level, True, self.sb.score)
            for ball in self.balls:
                ball.collide_with_paddle(self.paddle)
            for ball in self.balls:
                for i in range(len(self.bricks) - 1, -1, -1):
                    brick = self.bricks[i]
                    did_collide = ball.collide_with_object(brick)
                    if did_collide:
                        # Si la brique est un bonus ou un malus, appeler la méthode approprié
                        if brick.good:
                            self.apply_bonus()
                        elif brick.bad:
                            self.apply_malus()
                        elif not brick.unbreakable:
                            self.sb.increment()
                        brick.hit()
                        if brick.dead:
                            self.bricks.pop(i)
                            break
                    else:
                        self.bricks[i].draw()

        def on_keydown(self, key):
            """
            Gère les évènements KEYDOWN pour déplacer le paddle
            avec les touches correpondantes.

            key: Number or String - Numéro ou charactère du clavier
            """
            if key in ["q", "Q"]:
                self.paddle.isMovingLeft = True
            elif key in ["d", "D"]:
                self.paddle.isMovingRight = True
            elif key in ["p", "P"] and self.ready_to_toggle_pause:
                # ready_to_toggle_pause est un pour éviter que le menu pause
                # se cache et se montre à l'infini
                # Ce code ne pourra s'executer encore une fois si le joueur
                # lache la touche P
                self.ready_to_toggle_pause = False
                if self.playing_game:
                    self.show_overlay('pause')
                else:
                    self.hide_overlay()
            

        def on_keyup(self, key):
            """
            Gère les évènements KEYUP pour déplacer le paddle
            avec les touches correpondantes.

            key: Number or String - Numéro ou charactère du clavier
            """
            if key in ["q", "Q"]:
                self.paddle.isMovingLeft = False
            elif key in ["d", "D"]:
                self.paddle.isMovingRight = False
            elif key in ["p", "P"] and not self.ready_to_toggle_pause:
                # L'utilisateur lache la touche P, on est près a pauser/resumer
                self.ready_to_toggle_pause = True

    return Level

