# ÁREA = π · RAIO2, em que estão presentes as variáveis ÁREA, RAIO, a constante π (pi = 3.14159265)

pi = 3.14
raio = 10

area = pi * (raio ^ 2)

print(area)

print("-" * 30)
# a expressão X = { 43 · [ 55 : ( 30 + 2 ) ] } será escrita na forma computacional como X ← (43 * (55 / (30 + 2) ) ).

print((43 * (55 / (30 + 2) )))

print("-" * 30)
# A fórmula para o cálculo da área de um triângulo é definida como a expressão A ← (B * H) / 2.

base = 10
altura = 12

print("Área do triângulo: ", (base * altura) / 2)

print("-" * 30)
# Fórmula da Báskara
# DELTA ← B ↑ 2 - 4 * A * C
# X1 ← (- B + DELTA ↑ ( 1 / 2 ) ) / ( 2 * A )
# X2 ← (- B - DELTA ↑ ( 1 / 2 ) ) / ( 2 * A )

# Considere: 2x² - 5x + 2 = 0 a = 2, b = -5, c = 2.

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = b ^ 2 - (4 * a * c)
x1 = (- b + delta ** ( 0.5 )) / (2 * a)
x2 = (- b - delta ** (0.5) / (2*a))
print(x1)
print(x2)

## Não sei se está correto...