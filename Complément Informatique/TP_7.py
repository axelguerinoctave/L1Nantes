def inverser(l, compteur = []):
    print(l, compteur)
    if l == []:
        return compteur
    else:
        e = l.pop()
        compteur.append(e)
        return inverser(l, compteur)

l = list(range(10))
print(l)
print(inverser(l))