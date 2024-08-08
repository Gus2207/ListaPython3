'''1 – Para treinar o laço de repetição FOR, crie um formulário e peça para o usuário digitar
um número inicial e um número final, mostre o intervalo entre esses números, mas
lembre-se que ele poderá digitar um intervalo muito grande que irá consumir muita
memória do servidor, pensando nisso valide para que ele digite apenas intervalos de no
máximo 100 números.'''

inicial = int(input("Digite o número inicial: "))
final = int(input("Digite o número final: "))

while True:

    if (final > 100):
        final = int(input("O numero final não pode ser maior que 100, digite novamente: "))
    else:
        break;

for num in range(inicial, final + 1, 1):
    print(num)