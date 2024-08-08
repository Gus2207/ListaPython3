'''6 – Utilizando o Laço While imprima os 100 valores posteriores ao que o usuário digitou,
a cada 10 impressões crie uma forma elegante de separar os dados visualmente.'''

inicio = int(input("Digite o numero inicial: "))
limite = inicio + 100

while (inicio <= limite):
    inicio += 1
    if (inicio % 10 == 0):
        print("///------------------///")
    print(inicio)
    