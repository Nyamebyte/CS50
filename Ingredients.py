def main():
    name = order()
    print(f'Your total cost is ${name}')


def order():
    ingredients = {
        'Baja Taco': 4.00, 'Bowl': 8.50,
        'Burrito': 7.50, 'Nachos': 11.00,
        'Quesadilla': 8.50, 'Super Burrito': 8.50,
        'Super Quesadilla': 9.50, 'Taco': 3.00,
        'Tortilla Salad': 8.00
    }

    ordered_list = []
    while True:
        ing_order = input('What would you like to order?(Type exit when done) ').title()
        if ing_order == 'Exit':
            break
        ordered_list.append(ing_order)

    price = 0

    try:
        for item in ordered_list:
            cost = ingredients[item]
            price += cost
    except KeyError:
        print('At least 1 ingredient not found')
    return price


if __name__ == '__main__':
    main()
