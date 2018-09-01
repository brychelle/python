# Pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como 
# a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input("Quantos km foram percorridos? ")) * 0.15
dias = int(input("Quantos dias de aluguel? ")) * 60

print("Preço a pagar: R$ %.2f" %(km + dias))
