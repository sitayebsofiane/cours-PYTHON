#coding:utf-8
# la boucle while avec le mot breack et continue
jeu_lance=True
print("")
while jeu_lance:
    choixMenu=input("> ")
    if choixMenu=="again":
        #ici il continue et n'exicute pas le reste de la boucle et il revient au debut de la boucle 
        continue
    if choixMenu =="quitter":
        break
    print("tu es dans la booucle")
print("a bientôt")
# la boucle for
sentence="Bonjour tout le monde :) !"
for letter in  sentence:
    print(letter)
print(" a bientôt")
