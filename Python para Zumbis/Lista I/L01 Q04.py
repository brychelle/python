# Calcule o aumento de um salário
# Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Qual o salario? "))
percentual = float(input("Qual o percentual de aumento? "))

aumento = salario * (percentual / 100)

print("Vamor do aumento: R$ %.2f" %aumento)
print("Novo salário: R$ %.2f" %(salario + aumento))