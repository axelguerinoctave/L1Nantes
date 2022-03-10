from Materiel import Materiel


class Velo(Materiel):
    def __init__(self, id, tarif, dispo, taille, HF):
        super().__init__(id, tarif, dispo)
        self.taille = taille
        self.HF = HF

    def afficher(self):
        super().afficher()
        print("taille :", self.taille)
        print("HF :", self.HF)