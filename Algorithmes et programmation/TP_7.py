def remplir_liste():
    l = []
    n = int(input("Taille de la liste : "))
    i = 0
    while len(l) < n :
        i += 1
        e = float(input("Element " + str(i) + " : "))
        l.append(e)
    return l

def indice_min(l):
    for i in range(len(l)):
        if l[i] == min(l):
            return i 
    return 0

def tri_liste(l):
    r = []
    while l != []:
        e = min(l)
        r.append(e)
        l.pop(indice_min(l))
    return r

def tri_liste_r(l, r = []):
    if l == []:
        return r
    else:
        e = min(l)
        r.append(e)
        l.pop(indice_min(l))
        return tri_liste_r(l, r)

l = remplir_liste()
print(l)
print(tri_liste_r(l))