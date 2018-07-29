# Calcula a area de diversos objetos

pi = 3.14159
area = []
a, b, c = input().split(" ")

triangulo = (float(a) * float(c)) / 2
print("TRIANGULO:", format(triangulo, '.3f'))

circulo = pi * (float(c) ** 2)
print("CIRCULO:", format(circulo, '.3f'))

trapezio = ((float(a) + float(b)) * float(c)) / 2
print("TRAPEZIO:", format(trapezio, '.3f') )

quadrado = float(b) * float(b)
print("QUADRADO:", format(quadrado, '.3f'))

retangulo = float(a) * float(b)
print("RETANGULO:", format(retangulo, '.3f'))