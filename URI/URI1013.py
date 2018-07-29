# Retorna o maior numero entre três

a, b, c = input().split(" ")

maiorab = (int(a) + int(b) + abs(int(a)-int(b))) / 2
maior = (int(maiorab) + int(c) + abs(int(maiorab) - int(c))) / 2

print(int(maior), "eh o maior")