D = int(input())
#quantidades de dias que o ano mes e dia
quantidade_dias = [365,30,1]
resultado = []
for dia in quantidade_dias:
    qtd = int(( D /dia))
    resultado.append(str(qtd))
    D -= (qtd * dia)
print('ano(s)'.join(resultado[0]))
