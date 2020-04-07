
#liste des mots en francais
fr=['carte','chat','chien','courir','enfant','gros','jouet','maison','vert','voiture']
#liste des mot anglais correspondant
en=['card','cat','dog','run','kid','big','toy','home','green','car']
#dictionaire
dictionaire={}
#remplissage du dictionaire
for i in range(0,10):
    dictionaire.update({fr[i]:en[i]})
# initialisation du mot
mot=""
# la boucle while qui va demander a taper un mot et affiche sa traduction en anglais
while mot != "stop":
    mot=input("taper un mot parmis{}".format(fr)+" ou taper 'stop' pour arreté le programme: ")
    # je verifie si le mot existe dictionaire
    if mot in fr:
        print("le mot :",mot,"en anglais c'est",dictionaire[mot])
    # je previent avec un message en console si le mot n'exite pas
    elif mot !="stop":
        print("le mot '{}' n'existe pas dans mon dictionaire".format(mot))
    # et enfin quiter le programme
    else:
        print("au revoir...!")
