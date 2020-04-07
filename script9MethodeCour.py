#coding:utf-8

class Humain:
    
    lieu_habitation="US"

    def __init__(auto,nom,age):
        auto.nom=nom
        auto.age=age

    def parler(auto,message):#methode d'instance
        print("{} a dit : {}".format(auto.nom,message))
    
    def changer_place(cls,nouveau_lieu):#cls->methode de classe
        cls.lieu_habitation=nouveau_lieu
    changer_place=classmethod(changer_place)#le mot classmethod permet de determiner la methide de classe

    @classmethod
    def set_fine_amount(c,number = '20/20'):
        print(c,number)
    
    def definition():#methode static 
        print("l'homme n'est pas un mamefere mais un virus")        
    definition=staticmethod(definition)#la fonction qui permet la methode static

    @staticmethod
    def pluralize(number, sigular):
        assert isinstance(number, int) and number >= 0, 'le nombre doit etre positif'
        plural = sigular + 's'
        string = sigular if number <= 1 else plural
        return f'{number} {string}'

    def __str__(auto):
        return(f'{auto.nom} a {auto.pluralize(auto.age,"an")}')




#Programme principal
Humain.set_fine_amount()

h1 = Humain("jason",1)

h1.parler("Bonjour et salamalikoum")
print(h1)
Humain.changer_place("FR")
print("Lieu habitation est : {}".format(Humain.lieu_habitation))
Humain.definition()
