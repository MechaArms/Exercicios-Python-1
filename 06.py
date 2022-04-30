#exercício 6
#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

x = math.pi

raio = float(input("Por favor digite o numero do Raio do Círculo: "))

area = x * (raio ** 2)  # Área = Pi * Raio²

print(f'O número da Área do Círculo é: {area}')