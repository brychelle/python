# Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem

distancia = float(input("Qual a distancia da viagem? (km) "))
velocidade = float(input("Qual a velocidade media esperada? (km/h) "))

tempo = distancia / velocidade

print("Tempo de viagem calculado: ", tempo, "h")