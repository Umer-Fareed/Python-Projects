############## Scope #####################
enimies = 1

def increase_enimies():
    enimies = 2
    print(enimies)

increase_enimies()
print(enimies)


#local scope
# def drink_potion():
#     #local veriable
#     potion_srength = 2
#     print(potion_srength)
# drink_potion()

#global scope
# player_health = 10
# def game():
#     def drink_potion():
#         #local veriable
#         potion_strength = 2
#         print(player_health)
#     drink_potion()
#
# #there is no Block Scope
# game_level = 3
# def create_enemy():
#     enemies = ["skeleton", "zombie", "alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)


# enemies = 1
# """ Do not modify a global veriable for you local use inside a function
# you can use return statement instead of that
# """
# def increase_enemies():
#     return  enemies + 1
# enemies=increase_enemies()
# print(enemies)


# PI = 3.14159



