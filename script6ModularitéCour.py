#les fonctions lambda

ttc=lambda prixHT:prixHT+prixHT*20/100
print(ttc(24))
somme=lambda a,b: a+b 
print(somme(1,1))
#les modules sert a importer les module qui sert a utiliser certains fonction non  natives

import math
print(math.sqrt(100))
#on peut utiliser aussi from math import*ou [nom de la fonction]
from  module.moduleTest import parler as p,aurevoir
p("said","zoudj")
aurevoir()
'''# le module os pour importer les fonction du system
import os 
os.system("cls")'''