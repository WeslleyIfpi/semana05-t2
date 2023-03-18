def ehConsoante(letra):
    if letra in ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','w','y','z'):
        return True
    elif letra in ('B','C','D','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','V','X','W','Y','Z'):
        return True
    else:
        return False

def main():
    print('Este programa verifica se um caractere digitado é uma consoante.')
    entrada = input('Digite um caractere: ')
    print(f'{entrada} é uma consoante? {ehConsoante(entrada)}')

if __name__ == '__main__':
    main()