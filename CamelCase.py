def main():
    while True:
        name = input('Type in your username ')
        print(camel_convert(name))


def camel_convert(camel_str):
    # convert the first letter to lowercase
    snake_str = camel_str[0].lower()
    # iterating over the remaining characters
    for c in camel_str[1:]:
        if c.isupper():
            snake_str += '_'
        snake_str += c.lower()

    return snake_str


if __name__ == '__main__':
    main()
