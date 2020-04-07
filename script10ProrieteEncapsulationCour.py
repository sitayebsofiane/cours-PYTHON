#coding:utf-8
'''
Propriété : maniere  de manipuler/controler des attributs
            pricipe d'encapsulation !
'''
class Humain :

    def __init__(self,nom,age):
        print("Creation d'un humain...!")
        self.nom=nom
        self._age=age
    def _getage(self):#getter
        try:
            if self._age<=1:
                return str(self._age)+"an"
            else:
                return str(self._age)+"ans"

        except AttributeError:
            print("l'attribut age n'existe pas")
    def _setage(self,nouvel_age):#setter
        if nouvel_age<=0:
            self._age=0
        else:
            self._age=nouvel_age
    def _delage(self):#deleter
        del self._age
    # property(<getter>,<setter>,<deleter>,<helper>)
    age=property(_getage,_setage,_delage,"Je suis l'age d'un humain")

#Programme principal

h1=Humain("Jason",1)
print("{} a {}".format(h1.nom,h1.age))
h1.age=34
del h1.age
#help(Humain)
print(h1.nom)