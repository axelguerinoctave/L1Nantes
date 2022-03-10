from Materiel import Materiel


class Raquette(Materiel):
    def __init__(self, id, tarif, dispo, type_sport):
        super().__init__(id, tarif, dispo)
        self.type_sport = type_sport

    def afficher(self):
        super().afficher()
        print("type_sport :", self.type_sport)