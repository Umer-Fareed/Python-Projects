from  turtle import Turtle , Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)
timmy.left(90)
timmy.forward(90)
#object attributes
my_screen = Screen()
print(my_screen.canvheight)

#Object Methods
my_screen.exitonclick()

#########Cunstruct a pretty table object ##################
from  prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name ",["pikachu","squrtle","chermatic"])
table.add_column("type",["electric","water","fire"])
table.align = 'l'

print(table)
