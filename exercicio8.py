'''8 – Faça um while com uma condicional usando um booleano true, após 15 execuções
passe esse booleano para false para o while parar sua execução, cuidado para não deixar
dar loop infinito. Imprima o valor do booleano dentro do laço.'''

inicial = int(input("Digite o número inicial: ")) - 1
final = int(input("Digite o número final: ")) + 1
limite = inicial + 15
verificador = True

while (verificador == True):
    inicial += 1
    print(inicial)
    if(inicial == limite):
        verificador = False
        print(verificador)
