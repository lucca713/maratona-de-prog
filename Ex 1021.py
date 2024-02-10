valor = float(input())
#quantidades de dias que o ano mes e dia
quantidade_dias = [100, 50, 20, 10, 5, 2 , 1, 0.50, 0.25, 0.10, 0.05, 0.01]
resultado = []
for dia in quantidade_dias:
    qtd = int(( valor /dia))
    resultado.append(str(qtd))
    valor -= (qtd * dia)
    contador = 0
    print(f'{resultado[contador]} nota(s) de R$ {dia}\n')
