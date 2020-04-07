"""
python accepte l'hritage mulitple
"""
class Animal:
    def __init__(self,nom):
        self.nom=nom
    def manger(self):
        print(self.nom,"mange...")

class Reptile(Animal):
    def __init__(self,nom,regime_alim):
        Animal.__init__(self,nom)
        self.regime_alim=regime_alim
    #redifinition de la methode manger
    def manger(self):
        print("le reptile mange")
# heritage multiple
class Macron:
    pass
class Serpent(Animal,Macron):
    pass
    

#Programme
h1=Animal("lion")
h1.manger()
lezard=Reptile("lezard","grenouilles")
lezard.manger()
#connaitre si l'objet est une instance d'une classe
print(isinstance(lezard,Animal))
#connaitre si une classe est fille d'une autre 
print(issubclass(Reptile,Animal))