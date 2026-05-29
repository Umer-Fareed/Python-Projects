#password generator

import random
from random import shuffle

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
           'q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbels = ['!','@','#','$','%','^','&','*','(',')','+']
# print("wellcome to the password generator")
# nr_letters = int(input("Enter the number of letter you want to use: "))
# nr_symbels = int(input("Enter the number of symbels you want ot use: "))
# nr_numbers = int(input("Enter the number of numbers you want to use: "))
# password = " "
# for char in range(1,nr_letters+1):
#     password +=random.choice(letters)
#
# for num in range( 1, nr_numbers + 1):
#     password += random.choice(numbers)
#
# for sym in range(1 , nr_symbels + 1 ):
#     password += random.choice(symbels)
# print(password)

print("wellcome to the password generator")
nr_letters = int(input("Enter the number of letter you want to use: "))
nr_symbels = int(input("Enter the number of symbels you want ot use: "))
nr_numbers = int(input("Enter the number of numbers you want to use: "))
password_list =[]
for char in range(1,nr_letters+1):
    password_list +=random.choice(letters)

for num in range( 1, nr_numbers + 1):
    password_list += random.choice(numbers)

for sym in range(1 , nr_symbels + 1 ):
    password_list += random.choice(symbels)
    random.shuffle(password_list)

passwod = " "
for char in password_list:
    passwod += char

print(f"you final password is\n {passwod}\n thank you: ")