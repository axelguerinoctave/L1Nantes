def scalaire(u, v, compteur = 0):
    if u == [] or v == []:
        return compteur
    else:
        e_u = u.pop(0)
        e_v = v.pop(0)
        return scalaire(u, v, compteur + e_u * e_v)

u = [1, 2, 3]
v = [4, 5, 6]
print(u, v)
print(scalaire(u, v))