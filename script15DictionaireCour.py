#creation dictionaire
"""
    les erreur des dictionaire c'est KeyError
"""
dic={"clef1":"valeur1","clef2":"valeur2","clef3":"valeur3"}
print(dic["clef1"])
#ajout dans le dictionaire
dic["clef4"]="valeur4"
print(dic["clef4"])
#supression
val=dic.pop("clef3")
#ou
del dic["clef1"]
print(dic,val)
#verifiction existance clef
for cle in dic:
    if(cle=="clef2"):
        print("la cle existe")
#parcour sur toute les valeur
for val in dic.values():
    print(val)
#parcour dictionaire
for k,v in dic.items():
    print("Clé :{cle} -Valeur :{val}".format(cle=k,val=v))
#fonction qui produit un dictionaire
def maFonctionDic(**para):
    return para
dictionaire=maFonctionDic(p1=14,p2="note",p3="etc")
print(dictionaire)#dans les para il faut mettre nomVaraible p1,p2,p3..
print("les clefs sont",dictionaire.keys())#affiche les clefs 
#La méthode get permet de récupérer une valeur dans un dictionnaire et si
#  la clé est introuvable, on peut  donner une valeur à retourner par défaut:
data = {"name": "Wayne", "age": 45}
print(data.get("name"))
print(data.get("adresse", "Adresse inconnue"))
