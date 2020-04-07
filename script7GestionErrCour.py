#coding:utf-8
'''
    gerer les exptions: try/except(+else,finaly)

'''
#exemple1:
'''
 Type d'exeptions: ValueError
                   NameError
                   TypeError
                   ZeroDivisionError
                   OSError
                   AssertionError

'''
# si on connais pas le type de l'erreur on peut mettre juste le mot except
ageUser=input("entrez votre age:")
try:
    ageUser=int(ageUser) 
except:
    print("l'age indiqué est erroné")
else:
    print("tu as",ageUser,"ans")
finally:
    print("fin du programme")
#exemple2:
nbr1=150
nbr2=input("entrez le nombre pour diviser")
try:
    nbr2=int(nbr2)
    print("resultat = {}".format(nbr1/nbr2))
except ZeroDivisionError:
    print("larbi tu essaye de diviser par zero")
except ValueError:
    print("Vous devez entrer un nombre entier vous avez entré {}".format(nbr2))
finally:
    print("end of programe")
#exemple3 on peut creer un type d'expetion
#j'utiise le resultat de l'exemple1 ageUser
if ageUser <18:
    raise ValueError("interdit au moin de 18 ans ")
#les assertions
try:
    age=int(input("Quel age as-tu ? "))
    assert age<25
    print("age valide")
except AssertionError:
    print("l'age n'est pas dans l'assertion est superieur a 25") 

