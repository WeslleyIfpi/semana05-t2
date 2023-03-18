def ehNumeroOuLetra(entrada):
    return entrada.isalnum()

def main():
    print('Esse programa verifica se uma entrada é alfanumerica.')
    entrada = input('Digite um caractere: ')
    print(f'{entrada} é alfanumerico? {ehNumeroOuLetra(entrada)}')

if __name__ == '__main__':
    main()
