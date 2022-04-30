#exercício 16
'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

area = int(input("Por favor digite a área da parede em metros quadrados: ")) #funciona melhor para testar em multiplos de 3 com por exemplo 270 metros

litros = area / 3
latas = litros / 18
preco = latas * 80

print(f'O número de litros de tinta necessários é: {litros}')
print(f'A quantidades de latas de tinta a serem compradas é: {latas}')
print(f'O preço total é: R$ {preco}')