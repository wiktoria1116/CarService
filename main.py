from Car import Car

def main():
    while True:
        choice = menu()
        print(choice)
        if choice == "1":
            name = input("Enter car model:")
            year = input("Enter year:")
            buy_price = input("Enter buy_price:")
            sell_price = input("Enter sell price:")
            passat = Car(name, year, buy_price, sell_price)
            passat.add_car()
            print(passat)


def menu():
    print("What do you want to do?")
    print("1 - add car")
    choice = input("Enter your choice:")
    return choice


if __name__ == '__main__':
    main()

