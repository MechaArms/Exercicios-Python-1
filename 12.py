#exercício 12
#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Por favor digite a sua altura em metros: "))

peso = (72.7 * altura) - 58

print(f'o seu peso ideal é: {peso}')