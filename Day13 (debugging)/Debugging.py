##############debugging#####################3

#describe problem
# def my_function():
#     for i in range(1,21):
#         if i == 20:
#             print("you got it")
# my_function()


#Reproduce the bug
# from random import randint
# dice_images = ["#","!","$","@","&",")"]
# dice_num = randint(1,6-1)
# print(dice_images[dice_num])


#Play computer
# year = int(input("what's your year of birth "))
# if year > 1980 and year < 1994:
#     print("you are a millenial")
# elif year >= 1994:
#     print("you are a gen z ")


#Fix the error
# age = int(input("how old you are? "))
# if age > 18:
#     print(f"you can drive the age {age}.")


#Print is your friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


#Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
mutate([1,2,3,4,5,6,5])