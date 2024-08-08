'''5 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
inteiro entre 1 e 10. O usuário deve informar de qual numero ele deseja ver a tabuada.'''
tabuada = int(input('Digite a tabuada desejada (1 ao 10): '))
while True:
    if (tabuada > 10):
        tabuada = int(input('somente tabuadas do 1 ao 10, digite novamente: '))
    else:
        break;

resultado = 0

for num in range(1, 10 + 1, 1):
    resultado = tabuada * num
    print(f'{num} x {tabuada} = {resultado}')