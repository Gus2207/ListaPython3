'''3 – Peça para o usuário digitar um número, e mostre para ele se aquele é um número
primo ou não.'''

def main():
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo (ou '0' para sair): "))
            
            if numero == 0:
                print("Programa encerrado.")
                break
            
            if numero <= 1:
                print(f"O número {numero} não é primo.")
            elif numero == 2:
                print(f"O número {numero} é primo.")
            elif numero % 2 == 0:
                print(f"O número {numero} não é primo.")
            else:
                # Verifica se o número é primo
                is_primo = True
                limite = int(numero**0.5) + 1
                for i in range(3, limite, 2):
                    if numero % i == 0:
                        is_primo = False
                        break
                
                if is_primo:
                    print(f"O número {numero} é primo.")
                else:
                    print(f"O número {numero} não é primo.")
        
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()