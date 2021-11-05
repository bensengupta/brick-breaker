# coding=utf-8


from paddle_game.globals import Dimensions


class Button:
    """
    Classe pour faciliter l'affichage des boutons et la detection de clicks
    sur le bouton.
    """
    def __init__(
        self,
        x,
        y,
        text=None,
        width=Dimensions.WIDTH / 6,
        height=Dimensions.HEIGHT / 8,
        text_color='#ffffff',
        fill_color='#850010',
        stroke_color='#454545',
        stroke_weight=1,
    ):
        """
        Initialise un nouveau bouton.
        
        x: Number - Position X du coin en haut à gauche du bouton
        y: Number - Position Y du coin en haut à gauche du bouton
        text: String - (Optionnel) Texte affiché sur le bouton
        width: Number - (Optionnel) Largeur du bouton
        height: Number - (Optionnel) Longueur du bouton
        text_color: String - (Optionnel) Couleur du texte en couleur hexadecimal
        fill_color: String - (Optionnel) Couleur de remplissage en couleur hexadecimal
        stroke_color: String - (Optionnel) Couleur du contour en couleur hexadecimal
        stroke_weight: Number - (Optionnel) Epaisseur du contour
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill_color = fill_color
        self.stroke_color = stroke_color
        self.stroke_weight = stroke_weight
        self.text = text
        self.text_color = text_color
    
    def draw(self):
        """Affiche le bouton au coodonéées précisés à l'initialisation."""
        paddingX = self.width / 8
        paddingY = self.height / 8
        strokeWeight(self.stroke_weight)
        if self.stroke_color:
            stroke(self.stroke_color)
        if self.fill_color:
            fill(self.fill_color)
            rect(self.x, self.y, self.width, self.height)
        # Calculate text size
        fill(self.text_color)
        if self.text:
            textSize(12)
            minSizeW = 12 / textWidth(self.text) * (self.width - paddingX)
            minSizeH = 12 / (textDescent() + textAscent()) * (self.height - paddingY)
            textSize(min(minSizeW, minSizeH))
            offsetX = (self.width - textWidth(self.text)) / 2
            offsetY = (self.height - textDescent() - textAscent()) / 2
            text(self.text, self.x + offsetX, self.y + self.height - textDescent() - offsetY)
    
    def contains(self, pointX, pointY):
        """
        Revoir True si le point de coordonnée pointX et pointY est contenu
        dans le bouton.

        pointX: Number - Coordonné X du point
        pointY: Number - Coordonné Y du point
        """
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.width
        y2 = self.y + self.height
        return x1 <= pointX <= x2 and y1 <= pointY <= y2