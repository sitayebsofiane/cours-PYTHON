#coding:utf-8
# on a tout les operateur standard de comparaison
#condition multiple :and,or,in et not in
#exemple avec in
lettre_hasard="a"
if lettre_hasard not in "aeiouy":
    print("c'est une consonne")
else:
        print("c'est une voyelle")
var="25"
if not var==25:
    print("ok")
else:
    print("ko")
# une autre astuce
age=input("quel age as tu :")
age=float(age)
#je veux qu'il m'envoi un message validé si age et entre 0 et 100 sinon c'est invalide
#une fourchette de valeur
if 0<age<=100:
    print("valide")
else:
    print("invalide")
