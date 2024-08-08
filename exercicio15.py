'''15 - A estimativa feita pelos especialistas é que a perda acelerada de espécies que
presenciamos hoje está entre 1.000 e 10.000 vezes acima da taxa de extinção natural.
Esses especialistas calculam que entre 0,01 e 0,1% de todas as espécies são extintas por
ano.

Se considerarmos que a menor estimativa do número de espécies como verdadeira (isto
é, que existem mais ou menos 2 milhões de espécies diferentes em nosso planeta), isso
significa que todo ano ocorrem entre 200 e 2.000 extinções.

Porém, se a maior estimativa do número de espécies estiver correta (ou seja, que
existem 100 milhões de espécies diferentes convivendo conosco em nosso planeta),
então entre 10.000 e 100.000 espécies entram em extinção a cada ano.

Considerando os dados acima, desenvolva uma aplicação em que você considera os dois
cenários de pior e menos ruim taxa de extinção para cada estimativa do número de
espécies existentes. Calcule e mostre em quantos anos o ser humano vai ficar sozinho
no planeta junto com as baratas e pernilongos.'''

numeroEspecieMenor = 2000000
numeroEspecieMaior = 100000000

anosMenor = numeroEspecieMenor / 200
anosMenor2 = numeroEspecieMenor / 2000

print(f"No primeiro caso se houverem 2 milhões de espécies considerando 200 especies extinas por anos o ser humano firacá sozinho em {anosMenor} anos")
print(f"No primeiro caso se houverem 2 milhões de espécies considerando 2000 especies extinas por anos o ser humano firacá sozinho em {anosMenor2}")

anosMaior = numeroEspecieMaior / 10000
anosMaior2 = numeroEspecieMaior / 100000

print(f"No primeiro caso se houverem 100 milhões de espécies considerando 10000 especies extinas por anos o ser humano firacá sozinho em {anosMaior} anos")
print(f"No primeiro caso se houverem 100 milhões de espécies considerando 100000 especies extinas por anos o ser humano firacá sozinho em {anosMaior2} anos")