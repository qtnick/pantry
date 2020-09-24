pantry = {}

def add_item(item, quan):
    pantry[item] = quan


def list_pantry():
    print("That's what's in your pantry:")
    for item in pantry:
        print(f"{item}: {pantry[item]}")


def edit_pantry(item, quan):
    pantry[item] += quan

while True:
    answer = input("What would you like to do? ")
    if answer.lower() == "add":
        add_item(input("What would you like to add? "), int(input("How many? ")))
    elif answer.lower() == "quit":
        break
    elif answer.lower() == "list":
        list_pantry()
    elif answer.lower() == "subtract":
        edit_pantry(input("What would you like to change? "), int(input("Please, provide the quantity: ")))


list_pantry()
