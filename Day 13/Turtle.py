# import another_module
# print(another_module.another_variable)

from turtle import Turtle
import prettytable


# my_turtle = turtle.Turtle()

# my_screen = turtle.Screen()

# print(my_screen.canvheight)
# my_turtle.shape("turtle")
# my_turtle.color("chartreuse4")
# my_turtle.forward(100)
# my_screen.exitonclick()

table = prettytable.PrettyTable()

table.add_column("Pokemon",["Pikachu", "Squirtle", "Charmander"],"l")
table.add_column("Type", ["Electric", "Water", "Fire"],"r")

table.align = "c"

print(table)