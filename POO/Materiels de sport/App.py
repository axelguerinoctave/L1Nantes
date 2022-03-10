from Materiel import Materiel
from Raquette import Raquette
from Velo import Velo

materiel1 = Materiel(1, 12, True)
materiel2 = Materiel(2, 10, True)
raquette1 = Raquette(3, 15, True, "tennis")
velo1 = Velo(4, 20, True, 12, "H")
velo1.afficher()