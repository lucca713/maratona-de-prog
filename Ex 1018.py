notas001 = int(input())

notas100 = notas001//100
notas001 = notas001%100

notas50 = notas001//50
notas001 = notas001%50

notas20 = notas001//20
notas001 = notas001%20

notas10 = notas001//10
notas001 = notas001%10

notas05 = notas001//5
notas001 = notas001%5

notas02 = notas001//2
notas001 = notas001%2

print(f'{notas100} nota(s) de R$ 100,00')
print(f'{notas50} nota(s) de R$ 50,00')
print(f'{notas20} nota(s) de R$ 20,00')
print(f'{notas10} nota(s) de R$ 10,00')
print(f'{notas05} nota(s) de R$ 5,00')
print(f'{notas02} nota(s) de R$ 2,00')
print(f'{notas001} nota(s) de R$ 1,00')