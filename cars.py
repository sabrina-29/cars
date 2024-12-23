import os
import platform
from enum import Enum
import ast


class Actions(Enum):
    EXIT = 1
    ADD = 2
    DISPLAY = 3
    DELETE = 4
    FIND = 5
    DEL_ALL = 6
    

cars = []
FILE_NAME = 'cars.txt'


def save_cars_to_file():
    with open(FILE_NAME, 'w+') as f:
        # המרת רשימת המכוניות לסטירינג והוספת אותו לקובץ
        f.write(str(cars))
        print("File written successfully")


def read_cars_from_file():
    global cars
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            # קריאת תוכן הקובץ והמרתו חזרה לרשימה
            content = f.read()
            if content:
                cars = ast.literal_eval(content)  # המרת המחרוזת למבנה נתונים מתאים
    else:
        print("File does not exist. Starting with an empty list.")


def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def menu():
    print("\nMenu:")
    for act in Actions:
        print(f"{act.value} - {act.name}")
    try:
        user_selection = int(input("Your selection: "))
        return Actions(user_selection)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return None


def print_all_cars():
    if not cars:
        print("No cars to display.")
    else:
        for index, car in enumerate(cars):
            print(f"{index}: Model: {car['modle']}, Color: {car['color']}, Brand: {car['brand']}")
2

def add_cars():
    modle = input("Enter model: ")
    color = input("Enter color: ")
    brand = input("Enter brand: ")
    cars.append({"modle": modle, "color": color, "brand": brand})


def delete_car():
    print_all_cars()
    try:
        index_to_delete = int(input("Enter the index of the car to delete: "))
        if 0 <= index_to_delete < len(cars):
            del cars[index_to_delete]
            print("Car deleted successfully.")
        else:
            print("Invalid index!")
    except (ValueError, IndexError):
        print("Invalid input!")


def find_car():
    search_term = input("Enter the model, color, or brand to search: ").lower()
    found_cars = [car for car in cars if search_term in car['modle'].lower() or search_term in car['color'].lower() or search_term in car['brand'].lower()]
    if found_cars:
        for car in found_cars:
            print(f"Model: {car['modle']}, Color: {car['color']}, Brand: {car['brand']}")
    else:
        print("No cars found matching that search term.")


def delete_all_cars():
    global cars
    cars.clear()
    print("All cars have been deleted.")


if __name__ == "__main__":
    read_cars_from_file()
    while True:
        user_selection = menu()
        if user_selection is None:
            continue

        if user_selection == Actions.EXIT:
            save_cars_to_file()
            exit()

        elif user_selection == Actions.DISPLAY:
            print_all_cars()

        elif user_selection == Actions.FIND:
            find_car()

        elif user_selection == Actions.DELETE:
            delete_car()

        elif user_selection == Actions.ADD:
            add_cars()

        elif user_selection == Actions.DEL_ALL:
            delete_all_cars()

        save_cars_to_file()
