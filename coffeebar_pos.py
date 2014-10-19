__author__ = 'risinsun'


from transactions import *

items  = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.2, 1.80, 1.20]
running = True

while running:
    option = 1

    for choice in items:
        print(str(option) + ". " + items[option - 1])
        option = option + 1

    print(str(option) + ". Quit")

    choice = int(input("choose an option: "))

    if choice == option:
        running = False
    else:
        credit_card = input("Credit card number: ")
        save_transaction(prices[choice - 1], credit_card, items[choice - 1])