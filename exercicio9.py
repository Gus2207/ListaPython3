'''9 – Exercício Swap: esse exercício consiste em você criar 2 variáveis e colocar 1 nome de
pessoa em cada uma delas, faça um laço for onde a cada interação do laço as variáveis
troquem seu valor exemplo: $primeiroNome = “will”; $segundoNome = “lucas”; Na
primeira interação do laço, $primeiroNome terá o valor “lucas”, e $segundoNome o valor
“will”, e na segunda interação ao contrário e assim por diante. Imprima os valores a cada
interação utilizando var_dump para vermos o resultado.'''

primeiroNome = "Gustavo"
segundoNome = "Bento"
i = 0

while (i < 10):
    i += 1
    primeiroNome = "Gustavo"
    segundoNome = "Bento"
    print(primeiroNome)
    print(segundoNome)
    primeiroNome = "Bento"
    segundoNome = "Gustavo"
    print(primeiroNome)
    print(segundoNome)
