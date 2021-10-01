def bissextile(annee):
    A = (annee % 4) == 0
    B = (annee % 100) == 0
    C = (annee % 400) == 0
    return (A and (not B)) or C

def test():
    print("2021 : ", bissextile(2021))
    print("2020 : ", bissextile(2020))
    print("2000 : ", bissextile(2000))
    print("1900 : ", bissextile(1900))

def main():
    print("Veuillez entrer une année : ")

    annee = int(input())
    if bissextile(annee):
        print("L'année est bissextile")
    else:
        print("L'année n'est pas bissextile")

main()

