import math
import matplotlib.pyplot as plt

class Polygon:
    def __init__(self, n, summits = [], arcs = []):
        """
        Créer un polygone à n sommets. Si des sommets sont donnés, ils sont utilisés. Sinon, ils peuvent être générés avec la méthode generateSummits.
        """
        self.n = n
        self.summits = summits
        self.arcs = arcs
    
    def getAllArcs(self):
        """
        Retourne tous les arcs possibles du polygone.
        """
        
        arcs = []
        
        for i in range(self.n):
            for j in range(i + 2, self.n):
                arcs.append((i, j))

        return arcs
    
    def getSummitIndex(polygon, summit):
        """
        Retourne l'index du sommet summit dans le polygone polygon.
        """
        
        for i in range(len(polygon.summits)):
            if polygon.summits[i] == summit:
                return i
        
        return -1

    def generateSummits(self, radius):
        """
        Génère les sommets du polygone. Les sommets sont placés sur un cercle de rayon radius. Les sommets sont un tableau de tuple (x, y).

        Paramètres
        ----------
        radius : float
            Rayon du cercle sur lequel les sommets sont placés.
        """

        self.summits = []

        for i in range(self.n):
            self.summits.append((radius * math.cos(i * 2 * math.pi / self.n), radius * math.sin(i * 2 * math.pi / self.n)))

    def show(self):
        """
        Affiche le polygone.

        Remarque
        --------
        Les arcs sont affichés en rouge en pointillés. Les sommets sont affichés en bleu avec leur numéro.
        Utilise matplotlib.pyplot pour afficher le polygone.
        """

        summits = self.summits
        summits.append(summits[0]) # Pour former le polygone

        xs, ys = zip(*summits) # Convertir les sommets en deux tableaux (xs, ys)

        plt.figure()

        # Affiche les cordes
        for i, j in self.arcs:
            plt.plot([summits[i][0], summits[j][0]], [summits[i][1], summits[j][1]], linestyle='dashed', c='red')

        # Affiche les sommets
        for i in range(self.n):
            plt.text(summits[i][0], summits[i][1], str(i), fontsize=12, c='blue', fontweight='bold')
        plt.plot(xs, ys, c='black')

        plt.show()


if __name__ == "__main__":
    polygon = Polygon(5)
    polygon.generateSummits(1)
    polygon.arcs = [(0, 2)]

    print(polygon.summits)
    print(polygon.arcs)
    polygon.show()