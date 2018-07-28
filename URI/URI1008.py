# Calcula salario de funcionario com base nas horas trabalhadas

num = int(input())
horas = int(input())
valorhora = float(input())

salario = horas * valorhora

print("NUMBER = " + str(num))
print("SALARY = U$ %.2f" % salario)