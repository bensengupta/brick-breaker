# coding=utf-8


from paddle_game.utils.button import Button
from paddle_game.event import Event
from paddle_game.globals import Dimensions
from paddle_game.scene import Scene


class LevelMenuScene(Scene):
    """Menu de selectionnement de niveau."""
    def __init__(self, *scene_params):
        super(LevelMenuScene, self).__init__(*scene_params)
        self.add_event_handler(Event.MOUSE1, self.on_mouse1)
        self.level_buttons = []
        self.back_button = Button(
            Dimensions.WIDTH / 16,
            Dimensions.HEIGHT * 13 / 16,
            text='Menu Principal'
        )

    def get_max_level(self):
        level_to_evaluate = 1
        while self.check_scene_exist('level{}'.format(level_to_evaluate)):
            level_to_evaluate += 1
        return level_to_evaluate - 1

    
    def pre_display(self, *params):
        super(LevelMenuScene, self).pre_display(*params)
        highest_level = self.store.get('highest_level')
        max_level = self.get_max_level()
        for level in range(1, max_level + 1):
            self.level_buttons.append(
                (
                    'level{}'.format(level),
                    level <= highest_level,
                    Button(
                        Dimensions.WIDTH * 2 * (level % 6 + level // 6) / 13,
                        Dimensions.HEIGHT * 3/7 + Dimensions.HEIGHT * 2 * (level // 6) / 10,
                        width=50,
                        height=50,
                        text=str(level),
                        fill_color='#028500' if level <= highest_level else '#850010',
                    )
                )
            )

    def draw(self):
        background(0, 0, 0)
        fill('#ffffff')
        textSize(30)
        text("Niveaux", Dimensions.WIDTH / 2.9, Dimensions.HEIGHT / 5)
        textSize(40)
        for level, can_navigate, button in self.level_buttons:
            button.draw()
        self.back_button.draw()

    
    def on_mouse1(self, mouseX, mouseY):
        for button_level_number, can_navigate, button in self.level_buttons:
            if can_navigate and button.contains(mouseX, mouseY):
                self.reset_scene(button_level_number)
                self.set_scene(button_level_number)
        if self.back_button.contains(mouseX, mouseY):
            self.set_scene('start')