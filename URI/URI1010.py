# Recebe codigo, qtde e valor de dois produtos e retorna o valor total
# A entrada deve ocorrer em uma linha por item

a = []
a_code, a_qtty, a_price = input().split(" ")

b = []
b_code, b_qtty, b_price = input().split(" ")

total = ((float(a_price) * int(a_qtty)) + (float(b_price) * int(b_qtty)))

print("VALOR A PAGAR: R$ %.2f" % total)