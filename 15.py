#exercício 15
'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
A. salário bruto.
B. quanto pagou ao INSS.
C. quanto pagou ao sindicato.
D. o salário líquido.
E. alcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato (5%) : R$
    = Salário Liquido : R$
    Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
#26 dias uteis de 8 horas = 208 horas

val1 = float(input("Por favor digite o quanto você ganha por hora: ")) # 10 reais por hora trabalhada
val2 = float(input("Por favor digite o número de horas trabalhadas no mês: ")) # 200 horas

salbr = val1 * val2
ir = (11 / 100) * salbr
inss = (8 / 100) * salbr
sind = (5 / 100) * salbr
sallq = salbr - ir - inss - sind

print(f'+ Salário Bruto   : R$ {salbr}')
print(f'- IR (11%)        : R$ {ir}')
print(f'- INSS (8%)       : R$ {inss}')
print(f'- Sindicato (5%)  : R$ {sind}')
print(f'= Salário Liquido : R$ {sallq}')