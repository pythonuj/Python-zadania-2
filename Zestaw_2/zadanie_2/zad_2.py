def is_positive_number(input_string):
    liczba = input_string

    while not (liczba.isnumeric()):
        print()
        liczba = input("Niepoprawne dane, wpisz ponownie: ")

    return liczba


def is_in_range(liczba):
    while 1:
        if liczba < 1900 or liczba > 100000:
            liczba = input("\nLiczba nie nalezy do zakresu, wpisz ponownie: ")
            liczba = is_positive_number(liczba)
            break

    return liczba


def main():
    rok = input("Podaj rok z zakresu 1900 - 100000: ")
    rok = is_positive_number(rok)
    rok = is_in_range(rok)
    print("Wpisano: ", rok)


if __name__ == '__main__':
    main()