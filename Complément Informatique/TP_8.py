def produit_scalaire_vecteur(l, k, compteur = []):
    if l == []:
        return compteur
    else:
        compteur.append(l.pop(0) * k)
        return produit_scalaire_vecteur(l, k, compteur)

def produit_scalaire_matrice(l, k, compteur = []):
    if l == []:
        return compteur
    else:
        compteur.append(produit_scalaire_vecteur(l[0], k, []))
        l.pop(0)
        return produit_scalaire_matrice(l, k, compteur)

l = [1, 2, 3]
print(l)
print(produit_scalaire_vecteur(l, 2))


l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(l)
print(produit_scalaire_matrice(l, 2))

