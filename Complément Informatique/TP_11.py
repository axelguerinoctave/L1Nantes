arbre = {
    'valeur': 2,
    'gauche': {
        'valeur': 4,
        'gauche': {
            'valeur': 7,
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
        'valeur': 3,
        'gauche': None,
        'droite': None
    }
}

#print(arbre)

def parcours(arbre):
    if arbre == None:
        return 
    else:
        print(arbre['valeur'])
        parcours(arbre['gauche'])
        parcours(arbre['droite'])
    
#parcours(arbre)
import math
def max(arbre):
    if arbre == None:
        return 0
    else:
        gauche = max(arbre['gauche'])
        droite = max(arbre['droite'])
        valeur = arbre['valeur']
        if gauche > droite:
            if valeur > gauche:
                return valeur
            else: 
                return gauche
        else:
            if valeur > droite:
                return valeur
            else: 
                return droite

print('max =', max(arbre))