from validecorde import validecorde

def triangulation(C, cordes_tracées=[]):
    # extraire les sommets du polygone à partir de C
    sommets = list(set([s for c in C for s in c[:2]]))
    sommets.sort()
    
    # vérifier si le polygone est déjà triangulé
    if len(sommets) == 3:
        return cordes_tracées + [(sommets[0], sommets[1]), (sommets[1], sommets[2]), (sommets[2], sommets[0])]
    
    # explorer toutes les cordes possibles
    for c in C:
        corde = (c[0], c[1])
        
        if validecorde(corde, sommets, cordes_tracées):
            # tracer la corde
            cordes_tracées.append(corde)
            
            # diviser le polygone en deux sous-polygones
            i = sommets.index(c[0])
            j = sommets.index(c[1])
            gauche = sommets[i:j+1]
            droite = sommets[j:] + sommets[:i+1]
            
            # répéter le processus sur les sous-polygones
            gauche_triangulation = triangulation([c for c in C if c[0] in gauche and c[1] in gauche], cordes_tracées)
            droite_triangulation = triangulation([c for c in C if c[0] in droite and c[1] in droite], cordes_tracées)
            
            # retourner la triangulation complète
            return gauche_triangulation + droite_triangulation
    
    # si aucune corde n'est valide, le polygone est déjà triangulé
    return cordes_tracées