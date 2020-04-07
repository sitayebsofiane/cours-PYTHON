#coding:utf-8
#affichage d'un type d'une varaible
age=125
prix=121.23
lib='25'
boolean=True
print('le type de la variable est',type(lib))
#formater une chaine de caracter
texte = 'l''age de la personne est {} et le prix est {}€'.format(age,prix)
print(texte)
#la fonction qui revoi ce qui taper par le clavier en str
texte=input('entrez votre nom:')
print('bienvenu',texte)
#les fonction int() ,float(),str(),bool() ->permet de caster un element
print('a la base',lib,'le type a changé',type(int(lib)))
print(prix%3)