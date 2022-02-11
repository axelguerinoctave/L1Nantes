class Vehicule:
    def __init__(self, id, marque, annee_achat, prix_achat):
        self.id = id
        self.marque = marque
        self.annee_achat = annee_achat
        self.prix_achat = prix_achat
        
    def __str__(self):
        return 'id : ' + str(self.id) + ', marque : ' + self.marque + ', annee_achat : ' + str(self.annee_achat) + ', prix_achat : ' + str(self.prix_achat)
    

class Voiture(Vehicule):
    def __init__(self, id, marque, annee_achat, prix_achat, puissance, nb_portes, km):
        super().__init__(id, marque, annee_achat, prix_achat)
        self.puissance = puissance
        self.nb_portes = nb_portes
        self.km = km
        
    def prix_courant(self, an):
        prix = self.prix_achat
        prix *= pow(0.98, an - self.annee_achat)
        prix *= pow(0.95, round(self.km / 10000))
        if self.marque == 'Ferrari':
            prix *= 1.2
        if self.marque == 'Lada':
            prix *= 0.9
        return prix
        
    def __str__(self):
        return super().__str__() + ', puissance : ' + str(self.puissance) + ', nb_portes : ' + str(self.nb_portes) + ', km : ' + str(self.km)
    
class Avion(Vehicule):
    def __init__(self, id, marque, annee_achat, prix_achat, type_avion, nb_heures):
        super().__init__(id, marque, annee_achat, prix_achat)
        self.type_avion = type_avion
        self.nb_heures = nb_heures
      
    def prix_courant(self, an):
        prix = self.prix_achat
        if self.type_avion == 'helice':
            prix *= pow(0.9, round(self.nb_heures / 100))
        if self.type_avion == 'reaction':
            prix *= pow(0.9, round(self.nb_heures / 1000))
        return prix
        
    def __str__(self):
        return super().__str__() + ', type_avion : ' + self.type_avion + ', nb_heures : ' + str(self.nb_heures)

class Parc_Vehicule():
    def __init__(self):
        self.parc = []
        
    def rechercher(self, num):
        for vehicule in self.parc: 
            if vehicule.id == num:
                return vehicule
        return None
    
    def ajouter(self, v):
        if self.rechercher(v.id) == None:
            self.parc.append(v)
            
    def afficher(self):
        for vehicule in self.parc: 
            print(vehicule)
            
    def afficher_avion(self):
        for vehicule in self.parc: 
            if isinstance(vehicule, Avion):
                print(vehicule)
                
    def chercher_voiture(self, an, prix_max, nb_portes):
        for vehicule in self.parc:
            if isinstance(vehicule, Voiture):
                if vehicule.nb_portes == nb_portes and vehicule.prix_courant(an) < prix_max:
                    print(vehicule)

voiture1 = Voiture(1, 'Peugeot', 2008, 20000, 150, 5, 80000)
voiture2 = Voiture(2, 'Lada', 2003, 10000, 60, 3, 250000)
voiture3 = Voiture(3, 'Ferrari', 2016, 250000, 600, 3, 15000)
avion1 = Avion(4, 'Airbus', 1996, 250000000, 'reaction', 3000)
avion2 = Avion(5, 'Robin Aircraft', 1992, 100000, 'helice', 500)

parc = Parc_Vehicule()
parc.ajouter(voiture1)
parc.ajouter(voiture2)
parc.ajouter(voiture3)
parc.ajouter(avion1)
parc.ajouter(avion2)
parc.afficher()
