def somme_vecteur(u, v, compteur = []):
    return []

def somme_matrice(a, b, compteur = []):
    return []


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