import time
"""
print("premier message")
# la fonction sleep sert a faire dormir l'execution pour un thread
time.sleep(1)
print("deuxieme message")
"""
# afficher le timestamp nombre de second ecoulé depuis 01/01/1970 a 00h00
print(time.time())
# structure de temps en forme d'un tuple localtime(timstamp) prend en argument un timestamp
tps = time.localtime()

print(tps)
# mktime(localtime()) prend en parametre un localtime et retourne un timestamp
print(time.mktime(tps))
""" 
    manipuler les format de date  time.strftime():
    %d-->jour de 01 a 31
    %m-->mois de 1 a 12
    %Y-->année ex 2018 ,%y 00 a 99
    %H-->heure 00 a 23
    %M-->minutes 00 a 59
    %S-->second 00 a 59
    %p-->AM/PM
    %A: le nom du jour de la semiane %a jour abregé*
    %B: le nom du mois %b en abrégé
    %Z: fuseau horaire
"""
print(time.strftime("%A %B------%I"))