#exercício 18

#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arq = int(input("Digite o tamanho de um arquivo para download em MB: "))
spe = int(input("Digite a velocidade do seu link de Internet em Mbps: "))

tmps = arq / spe #tempo por segundo

tmpm = tmps / 60 #tempo por minuto

print(f'O tempo aproximado de download do arquivo é de {round(tmpm)} minutos')