segundos = int(input())

hora = int(segundos/ 3600)
segundos = int(segundos % 3600)
minuto = int(segundos / 60)
segundo = int(segundos % 60)

print("{}:{}:{}".format(hora,minuto,segundo))