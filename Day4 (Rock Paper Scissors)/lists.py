#list
States_of_america = ["delaware", "pennsylvenia", " washington"]
States_of_america[1]="havana "
print(States_of_america)
import random

#Who will pay the bill
name_string = input(" give me the everybody's name , seperated by a coma. ")
name = name_string.split(", ")
# x = len(name)
# random_choice =  random.randint(0 , x - 1  )
# person_choosen = name
person_chosen = random.choice(name)
print(f"{person_chosen} will pay the bill ")


#nested lists
dirty_dozen = ["strawberries", "spinach", "nectarines", "apples", "grapes", "peaches",
              "cherries", "pears", "tomatoes", "celery", "potatoes"]
fruits= ["strawberries",  "nectarines", "apples", "grapes", "peaches","cherries" ]
vegitalbes= ["pears", "tomatoes", "celery", "potatoes","spinach" ]
dirty_dozen = [fruits,vegitalbes]
print(dirty_dozen)

#hie the treasure
# row1 = ["☑","☑","☑"]
# row2 = ["☑","☑","☑"]
# row3 = ["☑","☑","☑"]
# map=[row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
#
# position = input("enter the position you want to hide ")
# horizontal = int(position[0])#2
# vertical = int(position[1])#3
# row = map[vertical-1]
# row[horizontal-1] = 'x'
# print(f"{row1}\n{row2}\n{row3}")