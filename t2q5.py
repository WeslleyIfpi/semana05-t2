def ehNumeroOuLetra(entrada):
    return not entrada.isalnum()

def main():
    print('Esse programa verifica se uma entrada contém um caractere especial.')
    entrada = input('Digite um caractere: ')
    print(f'{entrada} é/tem um caractere especial? {ehNumeroOuLetra(entrada)}')

if __name__ == '__main__':
    main()
