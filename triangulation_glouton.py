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

def triangulation_glouton(poly):
    triangles = []
    while len(poly.getAllArcs()) > 3: #tant que le polygone n'est pas un triangle
        min = None
        minI = None

        for i in range(len(poly.getAllArcs() - 2)):
            first = poly.summits[i]
            second = poly.summits[(i+1) % len(poly.getAllArcs())]
            third = poly.summits[(i+2) % len(poly.getAllArcs())]

            length = distance(first,third) / (2 * aire(first,second,third))

            if min == None or length < min:
                min = length
                minI = i

        # ajoute le nouveau triangle au array
        triangles.append((poly[minI], poly[minI+1], poly[minI+2]))
        
        # met à jour le polygone à trianguler
        if len(poly[:minI+1] + [poly[minI+2]]) == 3:
            poly = poly[:minI+1] + [poly[minI+2]]
        else:
            poly = [poly[minI]] + poly[minI+2:]

    triangles.append(tuple(poly))
    
    return triangles

if __name__ == "__main__":
    polygon = Polygon(7)
    polygon.generateSummits(1)
    polygon.show()
    
    print(triangulation_glouton(polygon))
    polygon.show()

