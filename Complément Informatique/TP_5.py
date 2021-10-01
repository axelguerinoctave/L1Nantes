def carre(x):
    return x * x

def map_list(l, f, compteur = []):
    if l == []:
        return compteur
    else:
        e = l.pop(0)
        compteur.append(f(e))
        return map_list(l, f, compteur)

liste = list(range(11))
print(liste)
print(map_list(liste, carre))