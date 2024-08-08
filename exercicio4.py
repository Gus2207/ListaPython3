'''4 - Peça para o usuário digitar outro intervalo, e agora mostre a soma entre os números
desse intervalo, lembre-se que o usuário não pode inserir um intervalo maior que 100
números.'''

inicial = int(input("Digite o número inicial: "))
final = int(input("Digite o número final: "))
resultado = 0
while True:
    if (final < 100 or inicial < 0):
        final = int(input("O número final não pode ser superior a 100, digite novemente: "))  
    else:
        for num in range(inicial, final + 1, 1):
            resultado += num
            print(f'o valor da soma dos numeros dentro do intervalo de {inicial} á {final} é {resultado}')