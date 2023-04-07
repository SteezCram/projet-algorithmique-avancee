from math import sqrt
from polygon import Polygon

class PolygonGlouton(Polygon):
    def distance(self, p1, p2):
        """
        Distance euclidienne entre deux points
        Source : https://fr.wikipedia.org/wiki/Distance_entre_deux_points_sur_le_plan_cart%C3%A9sien
        """

        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

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

        if (-s2_x * s1_y + s1_x * s2_y) != 0 and (-s2_x * s1_y + s1_x * s2_y) != 0:
            s = (-s1_y * (p1[0] - p2[0]) + s1_x * (p1[1] - p2[1])) / (-s2_x * s1_y + s1_x * s2_y)
            t = ( s2_x * (p1[1] - p2[1]) - s2_y * (p1[0] - p2[0])) / (-s2_x * s1_y + s1_x * s2_y)

            if s >= 0 and s <= 1 and t >= 0 and t <= 1:
                return True
        
        return False

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

def triangulation(polygon):
    allArcs = polygon.getAllArcs()

    while len(allArcs) > 0:
        shortest = None
        for arc in allArcs:
            if polygon.arcIsValid(arc[0], arc[1]):
                if shortest is None or polygon.distance(polygon.summits[arc[0]], polygon.summits[arc[1]]) < polygon.distance(polygon.summits[shortest[0]], polygon.summits[shortest[1]]):
                    shortest = arc
        
        if shortest == None:
            break

        polygon.arcs.append(shortest)
    
    return polygon.arcs


if __name__ == "__main__":
    polygon = PolygonGlouton(6)
    polygon.generateSummits(1)
    polygon.show()

    polygon.arcs = triangulation(polygon)
    print(polygon.arcs)
    polygon.show()