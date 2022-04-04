from math import inf
from Velo import Velo

class Magasin:
    
    def __init__(self):
        self.catalogue = []
        
    def ajouterMateriel(self, materiel):
        self.catalogue.append(materiel)
        
    def materielsDispo(self):
        for materiel in self.catalogue:
            if materiel.dispo:
                materiel.afficher()
                
    def rechercher(self, id):
        for materiel in self.catalogue:
            if materiel.id == id:
                return materiel
        return None
    
    def louer(self, id, duree):
        for materiel in self.catalogue:
            if materiel.id == id and materiel.dispo:
                materiel.dispo = False
                return materiel.prix(duree)
        return 0
    
    def meilleurVelo(self):
        id = 0
        min = inf
        for materiel in self.catalogue:
            if isinstance(materiel, Velo) and materiel.dispo:
                if materiel.tarif < min:
                    min = materiel.tarif
                    id = materiel.id
        return id
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    