'''7 – Faça um programa que peça um intervalo de no máximo 10 números e imprima esse
intervalo na ordem inversa, e depois na ordem correta.'''

inicio = int(input('Digite o número inicial: ')) 
inicio2 = inicio - 1
limite = int(input('Digit o número final: ')) + 1
limite2 = limite - 1

print("//------------------ordem inversa--------------------//")

for num in range(limite , inicio, -1):
    limite -= 1
    print(limite)

print("//------------------ordem correta--------------------//")

for num in range(inicio2, limite2, +1):
    inicio2 += 1
    print(inicio2)