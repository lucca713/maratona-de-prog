D = float(input())
#quantidades de dias que o ano mes e dia
quantidade_notas = [100.00, 50.00, 20.00, 10.00 ,5.00, 2.00]
quantidade_moeda = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
quantidade_que_coube = []
quantidade_que_coube_moeda = []
#calculo para saber o quanto sobre das notas
contador = 0
contador_moeda = 0
for nota in quantidade_notas:
    quantas_vezes_cabe = int((D/nota))
    quantidade_que_coube.append(str(quantas_vezes_cabe))

    #tenho que tirar as notas que couberam na primeira opcao em valor
    D -= (quantas_vezes_cabe*nota)
    
    if nota <= 2:
        for moeda in quantidade_moeda:
            quantas_vezes_cabe_moeda = int((D/moeda))
            quantidade_que_coube_moeda.append(str(quantas_vezes_cabe_moeda))
            D -=(quantas_vezes_cabe_moeda*moeda)
           

print('NOTAS:')
for nota in quantidade_notas:
    print(f'{quantidade_que_coube[contador]} nota(s) de R$ {nota:.2f}')
    #contagem para mudar o indice do valor
    contador = contador + 1

print('MOEDAS:')

for moeda in quantidade_moeda:
    print(f'{quantidade_que_coube_moeda[contador_moeda]} moeda(s) de R$ {moeda:.2f}')
    contador_moeda = contador_moeda + 1

    
   