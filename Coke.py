price = 50
while price > 0:
    coin_values = [5, 10, 25]
    coin = int(input('Insert coin:(5, 10, 25) '))
    if coin not in coin_values:
        print('Sorry, you did not insert a valid coin')
        break
    price = price - coin

    if price > 0:
        print(f'Amount due: {price}')
        print('Change due: 0')
    else:
        print('Amount due: 0')
        print(f'Change due: {abs(price)}')

