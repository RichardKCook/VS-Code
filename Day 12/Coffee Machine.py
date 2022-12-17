from menu import MENU
from menu import resources
COMP_KEYS = ["water", "coffee", "milk"]


def calc_cost(cost_to_collect):
    print("Please insert coins.")
    q = int(input("How many quarters?: "))*0.25
    d = int(input("How many dimes?: "))*0.10
    n = int(input("How many nickels?: "))*0.05
    p = int(input("How many pennies?: "))*0.01

    payment = q+d+n+p
    change = "{:.2f}".format(payment - cost_to_collect)
    if cost_to_collect < payment:
        resources["money"] += cost_to_collect
        print(f"\nYour change is {change}")
        return
    else:
        print("Sorry that's not enough money. Money refunded.")
        run()


def check_ingr(order):

    for key in COMP_KEYS:
        if resources[key] < order[key]:
            print("Sorry, not enough ingredients. Please make another selection")
            run()


def sub_ingr(order):

    for key in COMP_KEYS:
        resources[key] = resources[key] - order[key]


def make_coffee(request):

    order = MENU[request]
    check_ingr(order["ingredients"])
    calc_cost(order["cost"])
    sub_ingr(order["ingredients"])
    return


print("Welcome to the Coffee Machine!")


def run():

    sel = input(
        "What would you like to drink? Type 'espresso', 'latte', or 'cappuccino' ")

    if sel == "off":
        off = True
    elif sel == "report":
        print(resources)
        run()
    elif sel == "espresso" or sel == "latte" or sel == "cappuccino":

        make_coffee(sel)
        print(f"Here is your {sel}. Enjoy!")
        run()
    else:
        print("You didn't enter a valid selection")
        run()
    return


run()
