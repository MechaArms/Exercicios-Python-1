#exercício 11
'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
'''   
num1 = int(input("Por favor digite o primeiro número: "))
num2 = int(input("Por favor digite o segundo número: "))
num3 = float(input("Por favor digite o terceiro número: "))

resp1 = (num1 * 2) * (num2 / 2)
resp2 = (num1 * 3) + num3
resp3 = num3 ** 3

print(resp1)
print(resp2)
print(resp3)