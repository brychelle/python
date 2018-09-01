# Leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos

dias = int(input("Digite a quantidade de dias:")) * 86400
horas = int(input("Digite a quantidade de horas:")) * 3600
minutos = int(input("Digite a quantidade de minutos:")) * 60
segundos = int(input("Digite a quantidade de segundos:"))

total = dias + horas + minutos + segundos

print("Total em segundos", total)