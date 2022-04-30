#exercício 13
#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    #Para homens: (72.7*h) - 58
    #Para mulheres: (62.1*h) - 44.7

h = float(input("Por favor digite a sua altura em metros: "))
sexo = int(input("Por favor digite o seu sexo como 1 para masculino ou 2 para feminino: "))

if sexo == 1:
    peso = (72.7 * h) - 58
    print(f'o seu peso ideal é: {peso}')
elif sexo == 2:
    peso = (62.1 * h) - 44.7
    print(f'o seu peso ideal é: {peso}')
else:
    print(f'Erro, valor digitado errado em sexo')