def moyenne(liste): #fonction calculant la moyenne d'une liste
    somme = 0
    for valeur in liste:
        somme += valeur
    return somme / len(liste)

notes = []
n = int(input("Nb d'étudiants : "))
while len(notes) < n:
    note = float(input("Saisir note : "))
    if note >= 0 and note <= 20:
        notes.append(note)
    else:
        print("Mauvaise saisie !")
print("notes : ", notes)
print("moyenne: ", moyenne(notes))
print("moyenne: ", sum(notes)/ len(notes))