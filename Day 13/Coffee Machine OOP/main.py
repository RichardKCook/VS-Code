import coffee_maker
import menu
import money_machine


def run():

    order = input(
        "What would you like to drink? Type 'espresso', 'latte', or 'cappuccino' ")

    if order == "off":
        off = True
    elif order == "report":
        sel = coffee_maker.CoffeeMaker()
        sel.report()
        profit = money_machine.MoneyMachine()
        profit.report()
        run()
    elif order == "espresso" or order == "latte" or order == "cappuccino":

        itemMenu = menu.Menu()
        itemOrder = itemMenu.find_drink(order)
        coffeeMaker = coffee_maker.CoffeeMaker()
        moneymachine = money_machine.MoneyMachine()

        if moneymachine.make_payment(itemOrder,cost) == True:
            coffeeMaker.make_coffee(itemOrder)

        else:
            print("You didn't insert enough money")
            run()

    return


run()
