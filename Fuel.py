def main():
    digit = fuel_convert()
    if digit >= 0.9:
        print('F')
    elif digit <= 0.1:
        print('E')
    else:
        fuel_percentage(digit)


def fuel_convert():
    while True:
        fuel = input('Fraction:(x/y) ')
        try:
            a, b = (fuel.split('/'))
            fraction = int(a)/int(b)
            return fraction
            break
        except ValueError:
            print('Type a valid fraction')


def fuel_percentage(p):
    percentage = p*100
    return print(f'%{percentage}')





if __name__ == '__main__':
    main()