# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar

preco = float(input("Qual o valor da mercadoria? "))
percentual = float(input("Qual o percentual do desconto? ")) / 100

desconto = preco * percentual

print("Valor do desconto: R$ %.2f" %desconto)
print("Valor a pagar: R$ %.2f" %(preco - desconto))