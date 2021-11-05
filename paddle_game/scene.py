# coding=utf-8


class Scene(object):
    """
    Scene est une classe primordial au jeu. Toute action et effets visuels passent par l'intermédiaire
    des scènes. Pour voir un élément sur l'écran, il faut ajouter une nouvelle scène.
    """
    class Flags:
        """
        Options displonibles à la création de la scène.
        Permettent de communiquer au SceneManager certains comportements voulus.
        """
        OVERLAY_FREEZES_CHILD = 'overlay_freezes_child'
    
    def __init__(self, check_scene_exist, set_scene, show_overlay, hide_overlay, reset_scene, event_manager, store):
        """Initialise une nouvelle scène."""
        self.check_scene_exist = check_scene_exist
        self.set_scene = set_scene
        self.show_overlay = show_overlay
        self.hide_overlay = hide_overlay
        self.reset_scene = reset_scene
        self.__event_manager = event_manager
        self.store = store
        self.event_handlers = []

    def pre_display(self, *params):
        """
        Méthode appelé avant qu'une autre scène change de scène vers celui-ci.
        Prend des paramètres quelquonques et les ajoutes à la liste params
        pour être utilisé après par cette scène.

        params: Any - Paramètres de navigation vers cette scène
        """
        self.params = params
        # Tout les event handlers ajoutés dans __init__ sont activés
        # quand l'utilisateur navigue vers cette scène
        for handler in self.event_handlers:
            self.__event_manager.add_event_handler(handler)
    
    def post_display(self):
        """
        Méthode appelé avant que cette scène change de scène vers une autre scène
        """
        # Tout les event handlers ajoutés dans __init__ sont désactivés
        # quand l'utilisateur quitte cette scène
        for (id, name, type) in self.event_handlers:
            self.__event_manager.remove_event_handler(id)
    
    def add_event_handler(self, *params):
        """
        Ajoute un event handler à la liste d'event handlers.
        CB: Celui-ci serait actif uniquement pendant que la scène est actif.

        params: Any - Paramètres de création d'un event handler
        """
        self.event_handlers.append(self.__event_manager.create_event_handler(*params))
    
    def draw(self):
        """
        Méthode principale d'affichage pour la scène. Est appelé en boucle.
        """
        pass

    def freeze(self):
        """
        Méthode optionnelle pour pauser la scène. Est appelé lorsque un overlay
        est actif avec l'option Scene.Flags.OVERLAY_FREEZES_CHILD
        """
        pass

    def unfreeze(self):
        """
        Méthode optionnelle complémentaire à freeze() pour résumer la scène.
        """
        pass

    def reset(self):
        """
        Méthode optionnelle pour réinitialiser la scène. Une autre scène peut réinitialiser
        une autre scène avec self.reset_scene(nom_de_la_scene)
        """
        pass

class SceneManager():
    """Gère les changements de scène du jeu."""
    def __init__(self, initial_scene_name, scenes, overlays, event_manager, store):
        """
        Initialise un nouveau SceneManager.

        initial_scene_name: String - Nom de scène initiale
        scenes: (nom_scene: String, scene: Scene, flags: Scene.Flags)[]
                Liste de scènes pour le SceneManager
        overlays: (nom_overlay: String, overlay: Scene, flags: Scene.Flags)[]
                Liste d'overlay pour le SceneManager
                Note: les overlays sont légèrement différent des scènes,
                      ils peuvent êtres superposés sur des scènes
        event_manager: EventManager - Gère les évènements pour les scènes
        store: Store - Database du jeu
        """
        self.scenes = []
        self.overlays = []
        self.current_scene_name = initial_scene_name
        self.current_scene = None
        self.current_overlay_name = None
        for (name, scene_class, flags) in scenes:
            new_scene = (
                name,
                scene_class(
                    self.check_scene_exist,
                    self.set_scene,
                    self.show_overlay,
                    self.hide_overlay,
                    self.reset_scene,
                    event_manager,
                    store,
                ),
                flags
            )
            self.scenes.append(new_scene)
            if name == initial_scene_name:
                self.current_scene = new_scene[1]
                self.current_scene.pre_display()
        for (name, overlay_class, flags) in overlays:
            new_overlay = (
                name,
                overlay_class(
                    self.check_scene_exist,
                    self.set_scene,
                    self.show_overlay,
                    self.hide_overlay,
                    self.reset_scene,
                    event_manager,
                    store,
                ),
                flags
            )
            self.overlays.append(new_overlay)
    
    def check_scene_exist(self, scene_name):
        """
        Retourne si la scène en question existe, ou pas.

        scene_name: String - Nom de la scène à tester
        """
        for (name, scene, flags) in self.scenes:
            if name == scene_name:
                return True
        return False
    
    def set_scene(self, scene_name, *params):
        """
        Change la scène du jeu à nouvelle scene avec un nom de scène scene_name donnée.

        scene_name: String - Nom de la scène à naviguer
        params: Any - Paramètres de navigation à passer à la scène
        """
        for (name, scene, flags) in self.scenes:
            if name == scene_name:
                print("SceneManager: Setting new scene to '{}'".format(scene_name))
                self.current_scene.post_display()
                scene.pre_display(*params)
                self.current_scene_name = name
                self.current_scene = scene

    def reset_scene(self, scene_name):
        """
        Réinitialise une scène.

        scene_name: String - Nom de la scène a réinitialiser
        """
        for (name, scene, flags) in self.scenes:
            if name == scene_name:
                print("SceneManager: Resetting scene '{}'".format(scene_name))
                scene.reset()
    
    def show_overlay(self, overlay_name, *params):
        """
        Affiche un overlay.

        overlay_name: String - Nom de l'overlay à afficher
        params: Any - Paramètres de navigation à passer à l'overlay
        """
        for (name, overlay, flags) in self.overlays:
            if name == overlay_name:
                print("SceneManager: Showing overlay '{}'".format(overlay_name))
                self.current_overlay_name = name
                overlay.pre_display(*params)
                if Scene.Flags.OVERLAY_FREEZES_CHILD in flags:
                    self.current_scene.freeze()
                
    
    def hide_overlay(self):
        """Cache l'overlay."""
        for (name, overlay, flags) in self.overlays:
            if name == self.current_overlay_name:
                if Scene.Flags.OVERLAY_FREEZES_CHILD in flags:
                    self.current_scene.unfreeze()
                overlay.post_display()
        self.current_overlay_name = None
    
    def draw(self):
        """
        Méthode principale d'affichage, gouvernée par les méthodes de changement de scène
        et d'affichage d'overlay.
        """
        self.current_scene.draw()
        if self.current_overlay_name:
            for (name, overlay, flags) in self.overlays:
                if name == self.current_overlay_name:
                    overlay.draw()
        