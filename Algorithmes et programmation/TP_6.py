def getF1F2(genre):
    if genre == "H":
        return 0.7, 0.15
    if genre == "F":
        return 0.6, 0.1

def printparams(genre, masse, heure, n, f1, f2, taux, volumes):
    print("Paramètres")
    print("genre :", genre)
    print("masse :", masse)
    print("heure :", heure)
    print("n :", n)
    print("f1 :", f1)
    print("f2 :", f2)
    print("taux :", taux)
    print("volumes :", volumes)

def T(masse, heure, n, f1, f2, taux, volumes):
    somme = 0
    for i in range(n):
        somme += taux[i] * volumes[i]
    t =  (1000 * somme) / (masse * f1) - f2 * heure
    if t < 0:
        return 0
    else:
        return t
    

genre = input("Genre : ")
masse = float(input("Masse de l'individu : "))
heure = float(input("Temps depuis le premier verre : "))
n = int(input("Nombre de verres : "))
f1, f2 = getF1F2(genre)

taux = []
volumes = []

for i in range(n):
    v = float(input("Volume : "))
    t = float(input("Taux : "))
    taux.append(t)
    volumes.append(v)

printparams(genre, masse, heure, n, f1, f2, taux, volumes)

print("Taux :", T(masse, heure, n, f1, f2, taux, volumes))