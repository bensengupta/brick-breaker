# coding=utf-8


from paddle_game.utils.button import Button
from paddle_game.event import Event
from paddle_game.globals import Dimensions
from paddle_game.scene import Scene


class LevelEndOverlay(Scene):
    """Overlay de fin de niveau, apparait quand l'utilisateur gagne ou perd un niveau."""
    def __init__(self, *scene_params):
        super(LevelEndOverlay, self).__init__(*scene_params)
        self.continue_button = Button(
            Dimensions.WIDTH * 13 / 16,
            Dimensions.HEIGHT * 13 / 16,
            fill_color='#028500',
        )
        self.level_menu_button = Button(
            Dimensions.WIDTH / 2 - Dimensions.WIDTH / 12,
            Dimensions.HEIGHT * 13 / 16,
            text='Niveaux'
        )
        self.add_event_handler(Event.MOUSE1, self.on_mouse1)

    def draw(self):
        last_level_number, has_won_level, score = self.params
        has_won_game = has_won_level and not self.check_scene_exist('level{}'.format(last_level_number + 1))
        fill(0, 0, 0, 200)
        noStroke()
        rect(0, 0, Dimensions.WIDTH, Dimensions.HEIGHT)
        textSize(40)
        if not has_won_game:
            fill('#ededed')
            text('Niveau {}'.format(last_level_number), Dimensions.WIDTH / 3.3, Dimensions.HEIGHT / 2)
            textSize(30)
            if has_won_level:
                fill('#00ff00')
                text('Gagne', Dimensions.WIDTH / 3.3, Dimensions.HEIGHT / 1.7)
                self.continue_button.text = 'Continuer'
            else:
                fill('#ff0000')
                text('Perdu', Dimensions.WIDTH / 3.3, Dimensions.HEIGHT / 1.7)
                self.continue_button.text = 'Reessayer'
            fill('#a6a6a6')
            text('Score: {}'.format(score), Dimensions.WIDTH / 3.3, Dimensions.HEIGHT / 1.4)
            self.continue_button.draw()
        else:
            fill('#00ff00')
            text('Felicitations', Dimensions.WIDTH / 3.3, Dimensions.HEIGHT / 2)
            textSize(30)
            fill('#ededed')
            text('Vous avez gagne le jeu!', Dimensions.WIDTH / 3.3, Dimensions.HEIGHT / 1.7)
        self.level_menu_button.draw()
    
    def on_mouse1(self, mouseX, mouseY):
        last_level_number, has_won_level, score = self.params
        has_won_game = has_won_level and not self.check_scene_exist('level{}'.format(last_level_number + 1)) 
        if not has_won_game:
            if self.continue_button.contains(mouseX, mouseY):
                if has_won_level:
                    next_level_scene = 'level{}'.format(last_level_number + 1)
                    self.hide_overlay()
                    self.set_scene(next_level_scene)
                else:
                    this_level_scene = 'level{}'.format(last_level_number)
                    self.reset_scene(this_level_scene)
                    self.hide_overlay()
        if self.level_menu_button.contains(mouseX, mouseY):
            self.hide_overlay()
            self.set_scene('level_menu')
        