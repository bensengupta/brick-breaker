# coding=utf-8


class Line():
    """Classe pour stocker et manipuler les coordonnées d'une ligne."""
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def intersects_with_line(self, other):
        """
        Méthode vérifiant si cette ligne intersecte avec une autre ligne.
        Retourne True si il y a intersection et False si non.

        other: Line - Autre ligne à comparer
        """
        # Définir les points et s'assurer que (x1, y1) et (x3, y3) sont
        # les points les plus à gauche des lignes respectives
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        x3 = other.x1
        y3 = other.y1
        x4 = other.x2
        y4 = other.y2
        if x3 > x4:
            x3, y3, x4, y4 = x4, y4, x3, y3
        
        # S'assurer que les lignes ne sont pas verticales pour les calculs
        if x2 - x1 == 0:
            x1 = x2 - 0.00003
        if x4 - x3 == 0:
            x3 = x4 - 0.00003

        # Les lignes peuvent être chacunes représentés par une fonction affine
        # y = mx + p
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y4 - y3) / (x4 - x3)

        p1 = y1 - m1 * x1
        p2 = y3 - m2 * x3

        if m1 == m2:
            return False # Droites parrallèles donc intersection impossible
        
        # Calcul des coordonnées d'intersection des deux lignes
        x_inter = (p2 - p1) / (m1 - m2)
        y_inter = m1 * x_inter + p1

        ymin1, ymax1, ymin2, ymax2 = min(y1, y2), max(y1, y2), min(y3, y4), max(y3, y4)

        # Vérifie si l'intersection se passe dans les segments
        if (
            x1 <= x_inter <= x2
            and x3 <= x_inter <= x4
            and ymin1 <= y_inter <= ymax1
            and ymin2 <= y_inter <= ymax2
        ):
            print('INTERSECTION')
            return True
        # L'intersection se produit dans leur droite donc les segments ne se croisent pas
        return False