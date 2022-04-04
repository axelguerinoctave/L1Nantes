from Materiel import Materiel
from Raquette import Raquette
from Velo import Velo
from Magasin import Magasin

materiel1 = Materiel(1, 12, True)
materiel2 = Materiel(2, 10, True)
raquette1 = Raquette(3, 15, True, "tennis")
velo1 = Velo(4, 20, True, 12, "H")
velo2 = Velo(5, 15, True, 8, "F")

magasin = Magasin()

magasin.ajouterMateriel(materiel1)
magasin.ajouterMateriel(materiel2)
magasin.ajouterMateriel(raquette1)
magasin.ajouterMateriel(velo1)
magasin.ajouterMateriel(velo2)

"""
magasin.materielsDispo()

print("---------------------------------------")
print("prix : " + str(magasin.louer(3, 4)) + "€")
print("---------------------------------------")

magasin.materielsDispo()
"""

magasin.rechercher(magasin.meilleurVelo()).afficher()
