# Livro Algoritmo do Manzano: Página 140

# HT : horas trabalhadas no mês
# VH : valor hora-aula
# PD : percentual de desconto
# SB : salário bruto (SB), sendo a multiplicação das variáveis HT e VH.
# TD : total de desconto (TD) com base no valor de PD dividido por 100.
# SL : salário líquido (SL), deduzindo o desconto do salário bruto (SB)

HT = int(input("Horas trabalhadas no mês: "))
VH = int(input("Valor da Hora-aula: "))
PD = int(input("Percentual de Desconto do INSS: "))

SB = HT * VH
TD = (PD / 100) * SB
SL = SB - TD

print(f"Salário bruto:", SB)
print("Salário lígquido:", SL)

print("Desconto de", PD, "% do INSS:", TD)
