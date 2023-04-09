from polygon import Polygon

class PolygonEssaisSuccessifs(Polygon):
    def __init__(self, n, summits = [], arcs = []):
        """
        Créer un polygone à n sommets. Si des sommets sont donnés, ils sont utilisés. Sinon, ils peuvent être générés avec la méthode generateSummits.

        Paramètres
        ----------
        n : int
            Nombre de sommets du polygone.
        summits : list
            Liste des sommets du polygone.
        arcs : list
            Liste des arcs du polygone.
        """

        super().__init__(n, summits, arcs)
        self.arcsMax = (self.n * (self.n - 3)) // 2

    def arcIsValid(self, i, j):
        """
        Vérifie si l'arc (i, j) est valide. 3 vérifications sont effectuées :
        1. L'arc ne doit pas être un segment qui compose la figure.
        1. L'arc ne doit pas être un arc existant.
        3. L'arc ne doit pas intersecter un autre arc.

        Paramètres
        ----------
        i : int
            Numéro du premier sommet de l'arc.
        j : int
            Numéro du second sommet de l'arc.

        Retourne
        --------
        bool
            True si l'arc est valide, False sinon.
        """

        if i == j:
            return False
        
        # Vérifie que l'arc n'est pas un segment qui compose la figure
        if (i - 1) % self.n == j or (j - 1) % self.n == i:
            return False

        # Vérifie que l'arc n'est pas un arc existant
        if (i, j) in self.arcs or (j, i) in self.arcs:
            return False
        
        # Vérifie que l'arc ne coupe pas un autre arc
        for k, l in self.arcs:
            # Si un des sommets de l'arc est un sommet de l'arc existant, on passe à l'arc suivant
            if i == k or j == k or i == l or j == l:
                continue

            if self.doIntersect(self.summits[i], self.summits[j], self.summits[k], self.summits[l]):
                return False
            
        return True
    
    def divide(self, i, j):
        """
        Divise le polygone en deux sous-polygones.

        Paramètres
        ----------
        i : int
            Numéro du premier sommet de l'arc.
        j : int
            Numéro du second sommet de l'arc.

        Retourne
        --------
        Polygon, Polygon
            Sous-polygones gauche et droite.
        """
        
        gauche = self.summits[i:j+1]
        droite = self.summits[j:] + self.summits[:i+1]

        return PolygonEssaisSuccessifs(len(gauche), gauche, [(k, l) for k, l in self.arcs if k in gauche and l in gauche]), PolygonEssaisSuccessifs(len(droite), droite, [(k, l) for k, l in self.arcs if k in droite and l in droite])
    
    def doIntersect(self, p1, q1, p2, q2):
        """
        Vérifie si les segments [p1, q1] et [p2, q2] s'intersectent.

        Paramètres
        ----------
        p1 : tuple
            Premier sommet du premier segment.
        q1 : tuple
            Second sommet du premier segment.
        p2 : tuple
            Premier sommet du second segment.
        q2 : tuple  
            Second sommet du second segment.
        
        Retourne
        --------
        bool
            True si les segments s'intersectent, False sinon.

        Remarque
        --------
        Origine : https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
        """

        s1_x = q1[0] - p1[0]
        s1_y = q1[1] - p1[1]
        s2_x = q2[0] - p2[0]
        s2_y = q2[1] - p2[1]

        s = (-s1_y * (p1[0] - p2[0]) + s1_x * (p1[1] - p2[1])) / (-s2_x * s1_y + s1_x * s2_y)
        t = ( s2_x * (p1[1] - p2[1]) - s2_y * (p1[0] - p2[0])) / (-s2_x * s1_y + s1_x * s2_y)

        if s >= 0 and s <= 1 and t >= 0 and t <= 1:
            return True
        
        return False
    
def triangulation_essais_successifs(polygon, polygonAllArcs, polygonArcsCount = 0, summitIndex = 0):
    """
    Triangule le polygone en utilisant la méthode des essais successifs.

    Paramètres
    ----------
    polygon : PolygonEssaisSuccessifs
        Polygone à trianguler

    polygonAllArcs : list
        Liste des tous les arcs possibles

    polygonArcsCount : int
        Nombre d'arcs déjà tracés

    polygonSummits : list
        Liste des sommets du polygone à trianguler

    Retourne
    --------
    list
        Liste des arcs qui composent la triangulation
    """

    # Tant qu'on a pas tracé tous les arcs
    if summitIndex < polygon.arcsMax:
        triangulation_essais_successifs(polygon, polygonAllArcs, polygonArcsCount, summitIndex + 1)

    if polygon.arcIsValid(polygonAllArcs[summitIndex][0], polygonAllArcs[summitIndex][1]):
        # On ajoute l'arc à la triangulation
        polygon.arcs.append(polygonAllArcs[summitIndex])

        if polygonArcsCount == polygon.n - 3:
            # On retourne les arcs de la triangulation
            return polygon.arcs
        
        if summitIndex < polygon.arcsMax:
            # On a tracé une corde qui forme le polygone
            triangulation_essais_successifs(polygon, polygonAllArcs, len(polygon.arcs) + 1, summitIndex + 1)

    return polygon.arcs


if __name__ == "__main__":
    polygon = PolygonEssaisSuccessifs(6)
    polygon.generateSummits(1)
    polygon.show()
    
    polygon.arcs = triangulation_essais_successifs(polygon, polygon.getAllArcs())
    print(polygon.arcs)
    polygon.show()