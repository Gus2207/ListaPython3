'''14 - Crie um algoritmo que solicite um número, e faça o cálculo fatorial do mesmo, exiba
o resultado na tela.'''

numero = int(input("Digite o numero que deseja calcular o fatorial: "))
resultado = 1
for num in range(1, numero + 1, 1):
    resultado *= num
    
print(resultado)
