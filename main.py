import os

from Car import Car
import json
from prettytable import PrettyTable

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
        elif choice == "2":
            if os.path.exists("C:/Users/wikto/PycharmProjects/CarService/json_car_model.json"):
                file = open("json_car_model.json")
                data = json.load(file)
                print(data)
                cars_table = PrettyTable()
                cars_table.field_names = ["Id", "Name", "Buy price", "Sell price", "Year"]
                for i in data["car"]:
                    cars_table.add_row([i["id"], i["description"]['name'], i["description"]['buy_price'],
                                        i["description"]['sell_price'], i["description"]['year']])
                print(cars_table)


def menu():
    print("What do you want to do?")
    print("1 - add car")
    print("2 - show all cars")
    choice = input("Enter your choice:")
    return choice


if __name__ == '__main__':
    main()

