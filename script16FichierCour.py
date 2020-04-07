"""
modes d'overtture: r(lecture seule)
                   w(écriture avec remplacement)
                   a(écriture avec ajout en fin de fichier)
                   x(lecture et ecriture)
                   r+(lecture/ecriture dans un méme fichier)
                   wb(ecriture en binaire)
                   rb(lecture en binaire)
"""
#fic=open("module/donnees.txt","r")
# lire un fichier
#line=fic.readline() 

#content=fic.read()
#recuperer une seul ligne
#print(content)
print("-----")
#print(line)
#print(content)

#fic.close()
#une autre façon d'ouvrir un fichier
with open("module/donnees.txt","r") as fic:
    content=fic.read()
    print(content)
#le fichier est fermé ici7
#ecriture sur un autre fichier si le fichier n'existe pas il le cree
with open("module/bruno.txt","w") as fic:
    fic.write(str(15))
    fic.write("\nretour a la ligne")
#creation class joueur 
print("-----")
import pickle
class Player:
    def __init__(self,name,level):
        self.name=name
        self.level=level
    def whoami(self):
        print("{} ({})".format(self.name,self.level))
p1=Player("bruno",12)
p2=Player("thoma",15)
#ouvreture en ecriture binaire
"""
with open("module/data","wb") as fic:
    record=pickle.Pickler(fic)
    record.dump(p1) 
#ouverture en lecture binaire
with open("module/data","rb") as fic:
    record=pickle.Unpickler(fic)
    p1=record.load() 
p1.whoami()
"""