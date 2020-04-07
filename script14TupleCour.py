"""
liste=range(1,7)
for chose in enumerate(liste):
    print(chose)
2 raisons d'uliser les tuple: affectation multiple
                              retour multiple de fonction
"""
#creation de tuple
#un tuple avec une seul valeur <tple=(1233,)>
my_tuple =1,2,3
print(type(my_tuple))
#accees au valeurs d'un tuple 
print(my_tuple[1])
#affectation multiple
(n1,n2)=(14,16)
n1=12
print(n1)
#retour multiple de fonction
def get_postion():
    x=13
    y=26
    return x,y
res=poseX,poseY=get_postion()
print(res)