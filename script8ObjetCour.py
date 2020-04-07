#coding:utf-8

#creation de classe
class Humain:
    #Attribut lié a la classe
    humains_crees=0
    #constucteur
    def __init__(self,prenom,age):
        print("creation humain...",self) #affiche l'adresse ou se trouve l'objet avec le mot self
        self.prenom=prenom
        self.age=1
        Humain.humains_crees +=1
print("lancement du programme...")
h1=Humain("amar",45)
print("nombre humains crée {}".format(Humain.humains_crees))
print("prenom de h1 est {}".format(h1.prenom)) 
h2=Humain("rabah",45)
print("nombre humains crée {}".format(Humain.humains_crees))
print("prenom de h1 est {}".format(h1.prenom)) 