#Exercício 3.9

import datetime

data = datetime.date.today()
dia = int(data.day)
print("O dia atual é: %s" % dia)
horário = datetime.datetime.now()
hora = int(horário.strftime("%H"))
print("A hora atual é: %s" % hora)
minuto = int(horário.strftime("%M"))
print("O minuto atual é: %s" % minuto)
segundo = int(horário.strftime("%S"))
print("O segundo atual é: %s" % segundo)

convertM = minuto * 60
convertH = hora * 3600
convertD = dia * 86400

arr = [convertM, convertH, convertD]
Sum =  sum(arr)
segundos = Sum + segundo 

print("Isso tudo em segundos é igual à %s segundos." % segundos)
