codigo = float(input())
numero = float(input())
valor = float(input())

peca1 = [codigo,numero,valor]

codigo1 = float(input())
numero1 = float(input())
valor1 = float(input())

peca2 = [codigo1,numero1,valor1]

valor = (numero * valor) + (numero1 * valor1)

print('VALOR A PAGAR: R$ %.2f' %valor)

#ou

tatal = 0 

for i in range (2):
    item = input().split(" ")
    cod = int(item[0])
    qt = int(item[1])
    valor =  float(item[2])
    total = total + qt*valor
print('VALOR A PAGAR: R$ %.2f' %total)