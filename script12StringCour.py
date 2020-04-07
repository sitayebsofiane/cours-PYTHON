#coding:utf-8
# connaitre l'aide sur une classe
#les fonctions de la chaine travail sur une copie de celle ci
class  A(object):
    pass
#help(A)
#quelques methode de la class str
"""
    chaine.upper()->transfome la chaine en majuscule
    chaine.lower()->transfome la chaine en miniscule
    chaine.capitalize()->maj a chaque debut mot
    chaine.center()-> centrez une chaine de carater
    chaine.find(<chaine>,<debut>,<fin>)
    chaine.index(<chaine>,<debut>,<fin>)
    chaine.strip()->enleve espace
    chaine.replace(<oldstr>,<newstr>,<ocurence>)
    chaine.split("sperateur")->revoi une liste de mot separer avec le separateur
    chaine.isalpha()->si contient nombre
    chaine.islower()->si contient maj
    chaine.isupper()-> si contient min
    chaine.isidentifier()->si reserver au langauge python
    chaine.iskeyword()->
    chaine.isdecimal()->
    chaine.isnumeric()->
    chaine.isalphanum()->

    
"""
chaine="coco/ la/aarbi"
print(chaine.capitalize())
print(chaine.center(50,"-"))
print(chaine.replace("a","z",1))
print(chaine.split("/"))
print(chaine.isalpha())