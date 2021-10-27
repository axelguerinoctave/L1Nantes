def somme_vecteur_r(u, v, compteur = []):
    if u == [] or v == []:
        return compteur
    else:
        compteur.append(u.pop(0) + v.pop(0))
        return somme_vecteur(u, v, compteur)

def somme_matrice_r(a, b, compteur = []):
    if a == [] or b == []:
        return compteur
    else:
        compteur.append(somme_vecteur(a.pop(0), b.pop(0), []))
        return somme_matrice(a, b, compteur)

def somme_vecteur(u, v):
    r = []
    for i in range(len(u)):
        r.append(u[i] + v[i])
    return r

def Test():
    u = [2, 3]
    v = [5, 7]
    uplusv = [7, 10]
    if somme_vecteur(u, v) == uplusv:
        print("Test 1 : SUCCES")
    else:
        print("Test 1 : ECHEC")
    a = [[2, 3], [1, -3]]
    b = [[5, 7], [4, -7]]
    aplusb = [[7, 10], [5, -10]]
    if somme_matrice(a, b) == aplusb:
        print("Test 2 : SUCCES")
    else:
        print("Test 2 : ECHEC")

Test()