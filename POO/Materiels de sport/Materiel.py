from operator import truediv


class Materiel:
    def __init__(self, id, tarif, dispo):
        self.id = id
        self.tarif = tarif
        self.dispo = dispo

    def moinsCher(self, autre):
        return self.tarif < autre.tarif

    def prix(self, duree):
        return self.tarif * duree

    def afficher(self):
        print("id :", self.id)
        print("tarif :", self.tarif)
        print("dispo :", self.dispo)    