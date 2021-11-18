arbre = {
    'valeur': "*",
    'gauche': {
        'valeur': "+",
        'gauche': {
            'valeur': 3,
            'gauche': None,
            'droite': None
        },
        'droite': {
            'valeur': 1,
            'gauche': None,
            'droite': None
        }
    },
    'droite': {
        'valeur': 5,
        'gauche': None,
        'droite': None
    }
}

#print(arbre)

def parcours_prefixe(arbre):
    if arbre == None:
        return 
    else:
        print(arbre['valeur'])
        parcours_prefixe(arbre['gauche'])
        parcours_prefixe(arbre['droite'])

def parcours_infixe(arbre):
    if arbre == None:
        return 
    else:
        parcours_infixe(arbre['gauche'])
        print(arbre['valeur'])
        parcours_infixe(arbre['droite'])

def parcours_postfixe(arbre):
    if arbre == None:
        return 
    else:
        parcours_postfixe(arbre['gauche'])
        parcours_postfixe(arbre['droite'])
        print(arbre['valeur'])

"""
print("Prefixe :")
parcours_prefixe(arbre)
print("Infixe :")
parcours_infixe(arbre)
print("Postfixe :")
parcours_postfixe(arbre)
"""

def op(signe, x, y):
    if signe == "+":
        return x + y
    elif signe == "*":
        return x * y
    elif signe == "-":
        return x - y
    elif signe == "/":
        return x / y
    else:
        return 0

def calculer(arbre):
    if arbre["gauche"] == None or arbre["droite"] == None:
        return arbre["valeur"]
    else:
        return op(arbre["valeur"], 
                  calculer(arbre["gauche"]), 
                  calculer(arbre["droite"]))

print(calculer(arbre))