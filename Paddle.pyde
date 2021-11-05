from paddle_game.scenes.level_menu import LevelMenuScene
from paddle_game.store import Store
from paddle_game.scenes.level_end import LevelEndOverlay
from paddle_game.scenes.controls import ControlsScene
from paddle_game.scenes.pause import PauseOverlay
from paddle_game.globals import Dimensions
from paddle_game.scenes.levels import Level1, Level2, Level3, Level4, Level5, Level6, Level7
from paddle_game.event import Event, EventManager
from paddle_game.scenes.start import StartScene
from paddle_game.scene import Scene, SceneManager


def setup():
    global event_manager, scene_manager # on déclare la variable paddle comme globale
    size(Dimensions.WIDTH, Dimensions.HEIGHT)

    scenes = [
        ('start', StartScene, []),
        ('controls', ControlsScene, []),
        ('level1', Level1, []),
        ('level2', Level2, []),
        ('level3', Level3, []),
        ('level4', Level4, []),
        ('level5', Level5, []),
        ('level6', Level6, []),
        ('level7', Level7, []),
        ('level_menu', LevelMenuScene, []),
    ]
    
    overlays = [
        ('pause', PauseOverlay, [Scene.Flags.OVERLAY_FREEZES_CHILD]),
        ('level_end', LevelEndOverlay, [Scene.Flags.OVERLAY_FREEZES_CHILD]),
    ]

    event_manager = EventManager()
    store = Store()
    scene_manager = SceneManager('start', scenes, overlays, event_manager, store)


def draw():
    scene_manager.draw()

# détection des mouvements touches q et d
def keyPressed():
    event_manager.event(Event.KEYDOWN, key)

# annulation des mouvements quand on relâche la touche
def keyReleased():
    event_manager.event(Event.KEYUP, key)

def mousePressed():
    if mouseButton == LEFT:
        event_manager.event(Event.MOUSE1, mouseX, mouseY)
    elif mouseButton == RIGHT:
        event_manager.event(Event.MOUSE2, mouseX, mouseY)
    else:
        event_manager.event(Event.MOUSE3, mouseX, mouseY)
