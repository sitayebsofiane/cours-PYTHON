#coding:utf-8
# creation de fonction toujour commencer par mot clé def
def dire_bonjour(nom,prenom):
    print("Bonjour {} salam {}".format(nom,prenom))
#si je veut mettre parametre optionel
def dire_bonjour_para_optionel(nom,prenom=""):
    print("Bonjour {} salam {}".format(nom,prenom))
dire_bonjour_para_optionel("larab")
#si je veux traiter l'ordre des paramettre il faut specifier dans l'appel
def dire_bonjour_para_optionels(nom="",prenom="",age=0):
    print("Bonjour {} salam {} ton age est {}".format(nom,prenom,age))
dire_bonjour_para_optionels(age=14,nom="larab",prenom="youcef")#on a gerer l'ordre des parametre
#mettre pleusieur paramettre
def dire(*list_items):
    for item in list_items:
        print(item)
dire("salam","ok","hakim",25)
#fonction with return
def le_plus_grand(n1,n2):
    if(n1>n2):
        return n1
    elif n1==n2:
        pass
    else:
        return n2
print("le plus grand est {}".format(le_plus_grand(6,6)))