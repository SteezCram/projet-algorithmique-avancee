cordesTracees = []

def angle(i,j,k):
    ret = 1
    angle = (j[1]-i[1])*(k[0]-j[0]) - (j[0]-i[0])*(k[1]-j[1])
    if angle > 0:
        ret = 2
    elif angle < 0:
        ret = 0
    return ret

def validecorde(i,j):
    n = len(cordesTracees)
    for k in range(n):
        a, b = cordesTracees[k]
        if i == a or i == b or j == a or j == b:
            return True
        if angle(i, j, a) == angle(i, j, b) or angle(a, b, i) == angle(a, b, j):
            return True
        return False
