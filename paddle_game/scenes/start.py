# coding=utf-8


from paddle_game.utils.button import Button
from paddle_game.event import Event
from paddle_game.globals import Dimensions
from paddle_game.scene import Scene


class StartScene(Scene):
    """Scène de début du jeu, menu principal."""
    def __init__(self, *scene_params):
        super(StartScene, self).__init__(*scene_params)
        self.add_event_handler(Event.MOUSE1, self.on_mouse1)
        self.play_button = Button(
            Dimensions.WIDTH / 8,
            Dimensions.HEIGHT / 1.5,
            width=Dimensions.WIDTH / 2 - Dimensions.WIDTH / 4,
            height=40,
            text='Jouer',
            fill_color='#028500',
        )
        self.menu_button = Button(
            Dimensions.WIDTH / 2 + Dimensions.WIDTH / 8,
            Dimensions.HEIGHT / 1.5,
            width=Dimensions.WIDTH / 2 - Dimensions.WIDTH / 4,
            height=40,
            text='Niveaux',
        )
        self.controls_button = Button(
            Dimensions.WIDTH / 2 - Dimensions.WIDTH / 8,
            Dimensions.HEIGHT / 1.2,
            width=Dimensions.WIDTH / 2 - Dimensions.WIDTH / 4,
            height=40,
            text='Commandes',
        )

    def draw(self):
        background(0, 0, 0)
        textSize(40)
        fill("#0000ff")  # couleur de remplissage
        text("BRICK", Dimensions.WIDTH / 3, Dimensions.HEIGHT / 3)
        fill("#00ff00")  # couleur de remplissage
        text("BREAKER", Dimensions.WIDTH / 2.5, Dimensions.HEIGHT / 3 + 40)
        self.play_button.draw()
        self.menu_button.draw()
        self.controls_button.draw()
    
    def on_mouse1(self, mouseX, mouseY):
        if self.play_button.contains(mouseX, mouseY):
            highest_level = self.store.get('highest_level')
            self.set_scene('level{}'.format(highest_level))
        if self.controls_button.contains(mouseX, mouseY):
            self.set_scene('controls')
        if self.menu_button.contains(mouseX, mouseY):
            self.set_scene('level_menu')