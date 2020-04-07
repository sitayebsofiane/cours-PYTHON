#coding:utf-8
import datetime
""" datetime.datetime(year,month,day,hour,minute,second)"""
print('datetime.datetime(year,month,day,hour,minute,second)')
d1 = datetime.datetime(1985,1,1,5,52,23)
d2 = datetime.datetime(1985,1,1,5,52,0)
print(type(d2.year))

""" date sans les heurs et les minutes"""
print('date sans les heurs et les minutes')
d3 = datetime.date(1985,1,1)
print(d3,"l'annee",d3.year)
""" on peut travallier avec des temps les heurs et les minutes et les secondes"""
print('on peut travallier avec des temps les heurs et les minutes et les secondes')
t1 = datetime.time(23,00,46)
print(t1,"heurs:",t1.hour,"minutes:",t1.minute,"seconde:",t1.second)
""" affiche la date d'aujrdhui """
print('affiche la date d\'aujrdhui')
print(datetime.datetime.today(),"sans les heurs:",datetime.date.today())
""" calcluer mon age """
print('calcluer mon age')
naissance=datetime.date(1985,1,1)
aujrdhui=datetime.date.today()

print(f'mon age est :{aujrdhui.year-naissance.year} ans')

""" calculer mon age en secondes """
print('calculer mon age avec  secondes ')
naissance = d1
aujrdhui = datetime.datetime.today()

print(f'mon age est :{aujrdhui-naissance}')


