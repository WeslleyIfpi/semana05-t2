def ehLetra(entrada):
    return entrada.isalpha()

def main():
    print('Este programa verifica se um acractere digitado é uma letra.')
    entrada = input('Digite um caractere: ')
    print(f'{entrada} é letra? {ehLetra(entrada)}')

if __name__ == '__main__':
    main()