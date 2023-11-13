def main():
    time = convert(input("What is the time? "))
    if time <= 10:
        print('Breakfast')
    elif time <= 16.0:
        print('Lunch')
    elif time <= 21.0:
        print('Supper')
    else:
        print("It's too late or early for food")


def convert(time):
    hours, minutes = time.split(":")
    h = int(hours)
    m = int(minutes)
    time_converted = float(h + m / 60)
    return time_converted


if __name__ == '__main__':
    main()
