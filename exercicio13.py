'''13 - Você irá criar um laço de repetição que irá rodar 100 vezes mostrando os números
de 0 a 100. Porém o usuário através de um formulário colocará até que número ele quer
ver. Exemplo: usuário inserir 3 no formulário. Programa irá mostrar apenas os números
de 0 até 3, só irá mostrar até 100 se o usuário inserir 100 no formulário.'''

final = int(input("Digite em qual número deseja parar a repetição: "))

while True:
    if (final > 100):
        final = int(input("O número para parar a repetição não pode ser superior a 100, Digite novamente: "))
    else:
        break

i = 0
while (i < 100):
    i += 1
    for num in range(0, final +1, 1):
        print(num)