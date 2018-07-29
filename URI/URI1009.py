# Recebe Nome, Salario Fixo e Vendas e retorna o salario total com comissao

nome = input()
salario = float(input())
vendas = float(input())

comissao = vendas * 0.15

print("TOTAL = R$ %.2f" % (comissao + salario))