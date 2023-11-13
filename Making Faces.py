def main():
    text = input('What is your mood today? ')
    convert(text)


def convert(string_text):
    if string_text == ':)':
        print('🙂')
    elif string_text == ':(':
        print('🙁')
    else:
        print(string_text)


main()

