# coding=utf-8


from paddle_game.event import Event
from paddle_game.utils.button import Button
from paddle_game.globals import Dimensions
from paddle_game.scene import Scene


class PauseOverlay(Scene):
    """Overlay de pause, apparait quand l'utilisateur appuie sur P dans un niveau."""
    def __init__(self, *scene_params):
        super(PauseOverlay, self).__init__(*scene_params)
        self.unpause_button = Button(
            Dimensions.WIDTH * 13 / 16,
            Dimensions.HEIGHT * 13 / 16,
            fill_color='#028500',
            text='Resumer'
        )
        self.level_menu_button = Button(
            Dimensions.WIDTH / 2 - Dimensions.WIDTH / 12,
            Dimensions.HEIGHT * 13 / 16,
            text='Niveaux'
        )
        self.add_event_handler(Event.MOUSE1, self.on_mouse1)

    def draw(self):
        fill(255, 255, 255, 80)
        noStroke()
        rect(0, 0, Dimensions.WIDTH, Dimensions.HEIGHT)
        fill("#ffffff")
        bar_height = 50
        bar_width = 10
        bar_spacing = 3.5
        rect(Dimensions.WIDTH / 2 - bar_width - bar_spacing, Dimensions.HEIGHT / 2 - bar_height / 2, bar_width, bar_height)
        rect(Dimensions.WIDTH / 2 + bar_width + bar_spacing, Dimensions.HEIGHT / 2 - bar_height / 2, bar_width, bar_height)
        textSize(20)
        text("Appuyer sur P pour resumer", Dimensions.WIDTH / 3, Dimensions.HEIGHT / 1.5)
        self.unpause_button.draw()
        self.level_menu_button.draw()
        
    def on_mouse1(self, mouseX, mouseY):
        if self.unpause_button.contains(mouseX, mouseY):
            self.hide_overlay()
        elif self.level_menu_button.contains(mouseX, mouseY):
            self.hide_overlay()
            self.set_scene('level_menu')