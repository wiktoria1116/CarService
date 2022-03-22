from prettytable import PrettyTable
import json
import os.path


class Car:

    def __init__(self, name, buy_price, sell_price, year):
        self.name = name
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.year = year

    def __repr__(self):
        cars_table = PrettyTable()
        cars_table.field_names = ["Id", "Name", "Buy price", "Sell price", "Year"]
        cars_table.add_row([1, self.name, self.buy_price, self.sell_price, self.year])
        return str(cars_table)

    def add_car(self):
        description = {
            "name": self.name,
            "year": self.year,
            "buy_price": self.buy_price,
            "sell_price": self.sell_price
        }

        if os.path.exists("C:/Users/wikto/PycharmProjects/CarService/json_car_model.json"):
            file = open("json_car_model.json")
            data = json.load(file)
            car_id = 1
            for i in data["car"]:
                car_id = car_id + 1
            car_model = {"id": car_id, "description": description}
            data["car"].append(car_model)
            file.close()
            json_view = json.dumps(data, indent=4)
            with open('json_car_model.json', 'w') as file:
                file.write(json_view)
        else:
            car_model = {"car": [{"id": 1, "description": description}]}
            json_view = json.dumps(car_model, indent=4)
            with open('json_car_model.json', 'a') as file:
                file.write(json_view)




