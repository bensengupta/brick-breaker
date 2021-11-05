# coding=utf-8


from paddle_game.utils.button import Button
from paddle_game.event import Event
from paddle_game.globals import Dimensions
from paddle_game.scene import Scene


class ControlsScene(Scene):
    """Scène d'affichage de commandes pour jouer le jeu."""
    Controls = [
        'Q = Deplacer le paddle a gauche',
        'A = Deplacer le paddle a droite',
        'P = Mettre le jeu sur pause',
    ]

    def __init__(self, *scene_params):
        super(ControlsScene, self).__init__(*scene_params)
        self.back_button = Button(
            Dimensions.WIDTH / 16,
            Dimensions.HEIGHT * 13 / 16,
            text='Retour'
        )
        self.add_event_handler(Event.MOUSE1, self.on_mouse1)

    def draw(self):
        background(0, 0, 0)
        fill('#ffffff')
        textSize(30)
        text("Commandes", Dimensions.WIDTH / 3, Dimensions.HEIGHT / 5)
        textSize(20)
        for i, line in enumerate(ControlsScene.Controls):
            text(line, Dimensions.WIDTH / 6, Dimensions.HEIGHT / 14 * (i+5))

        self.back_button.draw()
    
    def on_mouse1(self, mouseX, mouseY):
        if self.back_button.contains(mouseX, mouseY):
            self.set_scene('start')
        