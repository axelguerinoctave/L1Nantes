def somme(liste, compteur = 0):
    print(liste, compteur)
    if liste == []:
        return compteur
    else:
        elem = liste.pop()
        return somme(liste, compteur + elem)

liste = list(range(10))
print(liste)
print("somme", somme(liste))