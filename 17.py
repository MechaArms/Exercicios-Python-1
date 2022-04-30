#exercício 17
'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    -comprar apenas latas de 18 litros;
    -comprar apenas galões de 3,6 litros;
    -misturar latas e galões, de forma que o desperdício de tinta seja menor. 
     Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

import math

area = int(input("Por favor digite a área da parede em metros quadrados: ")) 

litros = area / 6

latas = litros / 18
preco_lata = latas * 80

galao = litros / 3.6
preco_galao = galao * 25

lata_galao = (litros / 21.6) * 1.1 # (1 lata + 1 galão) + 10%

print(f'O número de litros de tinta necessários é: {math.ceil(litros)}')

print(f'A quantidades de latas de tinta a serem compradas é: {math.ceil(latas)}')
print(f'O preço total das tintas é: R$ {math.ceil(preco_lata)}')

print(f'A quantidades de galões de tinta a serem compradas é: {math.ceil(galao)}')
print(f'O preço total dos galões é: R$ {math.ceil(preco_galao)}')

print(f'A quantidades de latas e galões são de: {math.ceil(lata_galao)}')