from math import sqrt
from polygon import Polygon

def distance(p1,p2):
    """
    Distance euclidienne entre deux points
    Source : https://fr.wikipedia.org/wiki/Distance_entre_deux_points_sur_le_plan_cart%C3%A9sien
    """
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def aire(p1,p2,p3):
    """
    Calcul de l'aire d'un triangle
    """
    return abs((p2[0]-p1[0])*(p3[1]-p1[1]) - (p3[0]-p1[0])*(p2[1]-p1[1])) / 2

def triangulation(poly):
    copyPoly = poly
    
    while len(copyPoly.getAllArcs()) > 3: #tant que le polygone n'est pas un triangle
        min = None
        minI = None
        m = len(copyPoly.summits)

        for i in range(m-2):
            first = copyPoly.summits[i]
            second = copyPoly.summits[(i+1) % (m-2)]
            third = copyPoly.summits[(i+2) % (m-2)]

            length = distance(first,third) / (2 * aire(first,second,third))

            if min == None or length < min:
                min = length
                minI = i

        if (copyPoly.summits[minI], copyPoly.summits[minI+1]) not in poly.getAllArcs():
            poly.arcs.append((copyPoly.summits[minI], copyPoly.summits[minI+1]))
        
        if (copyPoly.summits[minI+1], copyPoly.summits[minI+2]) not in poly.getAllArcs():
            poly.arcs.append((copyPoly.summits[minI+1], copyPoly.summits[minI+2]))

        if (copyPoly.summits[minI], copyPoly.summits[minI+2]) not in poly.getAllArcs():
            poly.arcs.append((copyPoly.summits[minI], copyPoly.summits[minI+2]))
        
        # met à jour le polygone à trianguler
        if len(copyPoly.summits[:minI+1] + [copyPoly.summits[minI+2]]) == 3:
            copyPoly.summits = copyPoly.summits[:minI+1] + [copyPoly.summits[minI+2]]
        else:
            copyPoly.summits = [copyPoly.summits[minI]] + copyPoly.summits[minI+2:]
    
    return poly.arcs

if __name__ == "__main__":
    polygon = Polygon(7)
    polygon.generateSummits(1)
    polygon.show()
    
    polygon.arcs = triangulation(polygon)
    print(polygon.arcs)
    polygon.show()