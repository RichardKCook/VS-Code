from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine
off = False
items = Menu()
selection = items.get_items()
moneymachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
while not off:

    order = input(
        f"What would you like to drink? {selection}: ")

    if order == "off":
        off = True
    elif order == "report":
        
        coffeeMaker.report()
        
        moneymachine.report()
        
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        
        itemOrder = items.find_drink(order)
        
        if  coffeeMaker.is_resource_sufficient(itemOrder) == True:

            if moneymachine.make_payment(itemOrder.cost) == True:
                coffeeMaker.make_coffee(itemOrder)
            
            
            

