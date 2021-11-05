# coding=utf-8
from uuid import uuid4

class Event:
    """
    Classe utilisée pour définir des variables constantes pour être utilisés par les scènes,
    utile pour les events.
    """
    KEYUP = 'keyup'
    KEYDOWN = 'keydown'
    MOUSE1 = 'mouse1'
    MOUSE2 = 'mouse2'
    MOUSE3 = 'mouse3'

class EventManager():
    """
    Gère les évènements dans le jeu tel que les click de souris ou l'appuie d'une
    touche de clavier.
    """
    def __init__(self):
        """Initialise une instance de EventManager."""
        self.event_handlers = []
    
    def create_event_handler(self, event_name, event_handler):
        """
        Crée un nouveau event handler.

        Note: pour l'ajouter à la liste d'event handlers, utiliser add_event_handler

        event_name: Event.* - Nom de l'évènement à écouter
        event_handler: Function - Fonction appelé dès que l'évènement est déclanché

        return (id: String, event_name: String, event_handler: Function)
        """
        id = uuid4()
        return (id, event_name, event_handler)
    
    def add_event_handler(self, event_handler):
        """
        Ajoute un event handler crée précédemment avec create_event_handler à la liste
        d'event handlers.

        event_handler: (id: String, event_name: String, event_handler: Function)
        """
        self.event_handlers.append(event_handler)
    
    def remove_event_handler(self, id):
        """
        Supprimer un event handler de la liste en cherchant l'id donné

        id: String - L'id de l'event handler donnée à la création de celui-ci
        """
        for (index, handler) in enumerate(self.event_handlers):
            if handler[0] == id:
                self.event_handlers.pop(index)
                break

    def event(self, event_name, *params):
        """
        Déclanche un évènement pour être pris en main par les event handlers

        event_name: Event.* - Nom de l'évènement
        params: Any - Données associés à l'évènement

        ex: EventManager.event('mouse1', mouseX, mouseY)
        """
        for (handler_id, handler_event_name, event_handler) in self.event_handlers:
            if handler_event_name == event_name:
                event_handler(*params)

