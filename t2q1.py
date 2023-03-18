def ehVogal(letra):
    if (letra == 'a') or (letra == 'e')  or (letra == 'i') or (letra == 'o') or (letra == 'u'):
        return True
    elif (letra == 'A') or (letra == 'E')  or (letra == 'I') or (letra == 'O') or (letra == 'U'):
        return True
    else:
        return False

def main():
    print('Este programa verifica que se um caractere digitado é vogal.')
    entrada = input('Digite um caractere: ')
    print(f'{entrada} é volgal? {ehVogal(entrada)}') 

if __name__  == '__main__':
    main()