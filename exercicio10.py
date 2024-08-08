'''10 - Faça um laço de repetição simulando a corrida entre dois carros, o carro 1 iniciará
sua velocidade com 10 km/h, e o carro 2 iniciará com 20 km/h. Considerando que o carro
1 ganha 3 km/h a cada volta, e o carro 2 ganha 1,5 km/h a cada volta. Em quantas voltas
o carro 1 ultrapassará o carro 2? Imprimia a velocidade atual dos carros a cada interação
do laço e o número da volta. Imprima no final a quantidade total de voltas.'''
carro1 = 10
carro2 = 20
contador = 0

print("o carro 1 iniciará a 10 km/h")
print("o carro 2 iniciará a 20 km/h\n")

while True:
    carro1 += 3
    carro2 += 1.5
    contador += 1

    print(f"Na {contador}° volta o carro 1 atingiu {carro1} km/h, enquanto o carro 2 atingiu {carro2} km/h")

    if(carro1 > carro2):
        print(f"A corrida terminou na {contador}° volta com o carro 1 á {carro1} km/h e o carro 2 á {carro2} km/h")
        break