#Data Types

#string
print("hello"[2:4])

#Integer
print(123)
print(1_2_3)

#Float
print(12.42)

#Boolean


#Type Casting
num_char = len(input("type your name here "))
new_num_char = str(num_char)
print("the character in your name are " + new_num_char)

#input number and add them each other
user_input = input("enter a number ")
num_1=int(user_input[0])
num_2=int(user_input[1])
result=num_1+num_2
print(result)

#BMI
hight=input("enter your hight in meters")
weight= input("enter your weight in kilograms")
hight_up=float(hight)
weight_up=int(weight)
height=hight_up**hight_up
BMI=weight_up/height
print("your BMI is " + str(BMI))

#f-string
score = 0
height =3.22
inMatch = True
print(f"your score is {score}, and your wight is {height}" )

#Remaining age
age=input("what is your current age ")
t_age = 4680
age_up=int(age)
age_up1=age_up*52
remaining_age =t_age-age_up1
print(f"your remaining age is {remaining_age}, weeks")


