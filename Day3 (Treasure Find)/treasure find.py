#Treasure island
print('''
 *******************************************************************************
           |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("welcome to treasure island. ")
print("Your mission is to find treasure. ")
choice1=input("you're at a crossroad, where do you want to go?\n Type 'left or 'write:  ")

if choice1 == 'left':
   choice2=input("you've come to a lake."
                 " there is an island in the middle of the lake.\n"
                 " type 'wait' to wait for a boad.\n type 'swim' to"
                 " swim across: ").lower()
   if choice2=='wait':
       choice3=input("you are arrive at the iceland unharmed.\n"
                     " there is a house with 3 doors.\n One red,"
                     " One yellow, and one blue: ").lower()
       if choice3=='red':
           print("it's a room full of fire. Game over ")
       elif choice3=='yellow':
           print("you find the treasure you win. ")
       elif choice3=='blue':
           print("you choice a door that doesn't exist . Game over ")
       else:
        print("you got attacked by angry animal. Game over ")
   else:
        print("you attacked by an angry traut. Game over  ")
else:
    print("you fall into a hole game over. ")