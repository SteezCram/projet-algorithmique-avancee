# projet-algorithmique-avancee-2023
Projet d'algorithme avancée - Thomas CROIZET et Gurwan DELAUNAY

## Description
Code du projet d'algorithme avancée. Chaque type d'algorithme est dans un fichier séparé nommé par le nom de l'algorithme. Le fichier `polygon.py` contient une classe `Polygon` qui permet de créer des polygones et de les manipuler. Elle implémente la structure ayant le même nom décrite dans le compte-rendu du projet. Chaque algorithme recréer une classe héritant de la classe `Polygon` et implémentant des méthodes spécifiques à l'algorithme.

## Installation
Pour installer le projet vous devez avoir python 3.9.1 minimum d'installé sur votre machine. Vous pouvez le télécharger [ici](https://www.python.org/downloads/release/python-391/). Assurez-vous d'installer PIP en même temps. Pour lancer le projet vous aurez besoin du paquet `matplotlib` qui permet de tracer des graphiques. Pour l'installer, ouvrez un terminal et tapez la commande suivante :
```bash
pip install matplotlib
```

## Utilisation
Pour utiliser le projet, vous pouvez lancer directement chaque fichier python. Pour cela, ouvrez un terminal et tapez la commande suivante :
```bash
python nom_du_fichier.py
```

Chaque fichier contient un code à exécuter situé dans la fonction `main()`. Celui-ci contient un petit exemple sur un polygone en particulier pour voir le fonctionnement de l'algorithme. Vous pouvez modifier ce code pour tester d'autres polygones.

Pour cela, vous pouvez créer manuellement un polygone en créer un objet polygone via `PolygonAlgorithmeGlouton|PolygonEssaisSuccessifs|PolygonProgrammationDynamique(n)` où `n` est le nombre de côté du polygone en mettant des coordonnées `(x, y)` dans la liste `summits`.

Pour créer un polygone régulier, vous pouvez utiliser la méthode `generateSummits(radius)` où `radius` est le rayon du cercle dans lequel le polygone est inscrit après création de l'objet.

Des commentaires sont présents dans le code pour expliquer le fonctionnement de chaque fonctions et méthodes.