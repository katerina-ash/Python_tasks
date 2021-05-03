name = str(input('Введите имя: '))

def has_vower():
    if set('aeiou').intersection(name.lower()):
        print('Имя содержит гласную.')
    else:
        print('Имя не содержит гласнуюю')

def print_letters():
    for letter in name:
        print(letter)

def main():
    has_vower()
    print_letters()

if __name__ == '__main__':
    main()