liste=list()
liste.insert(1,1) 
liste.insert(0,"zero")
liste.insert(2,"deux")
liste.insert(3,"trois")
try:
    i=int(input("entrez la postion : "))
except TypeError:
    print("error")

print(liste[-len(liste):i-len(liste)])
#modifier les 2 premier element
liste[:4]=["modif"]*4
print(liste)
#transfomer liste en chaine
mots=["salam","alikoum"]#a condition que les element soit des chaines
print("_".join(mots))
#creer une liste independes de la premiere
import copy
mots_copie=copy.deepcopy(mots)
print(mots_copie)
mots_copie.append("ajout")
print(mots)
print("la liste copie apres l'ajout",mots_copie)
#ajout d'une liste a la suite d'une autre
mots_copie.extend(mots)#ça revient a faire mots_copie=mots_copie+mots
print(mots_copie) 