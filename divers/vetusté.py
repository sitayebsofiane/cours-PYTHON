#coding:utf-8
def calcul_prix(anné_achat,coef,prix):
    nbr=2019-anné_achat
    while nbr>0:
        nbr -=1
        prix *=1-coef
    return prix


a=int(input('entrez année d''achat '))
b=float(input('entrez coef '))
c=float(input('entrez prix '))
print('le prix qui sera rembousé est {}'.format(calcul_prix(a,b,c)))
