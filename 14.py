#exercício 14
'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.

se > 50 pague R$ 4,00 por kg extra
'''
peso = float(input("Por favor digite peso em Kg de peixes obtidos: "))
exdt = float
multa = float

if peso > 50:
    exdt = peso - 50
    multa = 4 * exdt
    print(f'O peso tem um excedente de : {exdt} Kg')
    print(f'O valor de sua multa é de : R$ {multa}')
else:
    print(f'Peso sem excedente.')