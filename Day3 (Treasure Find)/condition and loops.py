 #if-else statement
print("well come here ")
height = int(input("what is your hiehgt"))
if height > 120:
    print("you can go for it ")
else:
    print("sorry you can not ")

#check odd or even
print("well come back ")
num = int(input("enter a number "))
if num%2==0:
    print("Your number is even ")
else:
    print("your number is odd ")


#nested if
height = int(input("enter your height"))
if height >= 120:
    age = int(input("enter your age "))
    if age >= 18:
        print("wellcome to the rolarcoaster")
    else:
        print("sorry you are not elligable ")
else:
    print("you are not elliable ")

#BMI calculator and suggestion
height=float(input("enter the hieght in metter"))
weight=int(input("enter weight in kilograms"))
bmi=weight/height**2
if bmi < 18.5:
    print("you are under weight")
elif bmi >18 | bmi <=25:
    print("you are normal weight")
elif bmi >25 | bmi <= 30:
    print("you are over wieght")
elif bmi >30 | bmi <= 35:
    print("you are obese")
else:
    print("you are clinically obese")

#leap year check
year = int(input("enter the year "))
if year % 4 == 0 & year & 100 == 0 & year & 400 == 0:
    print("yaer is leap year ")
else:
    print("year is not leap year ")

#pizza bill counter
print("well come to pizza delivery ")
size = input("what size do you want ? 's', 'm', 'l'  ")
add_pepperoni = input("do you want to add pepperoni? 'y', 'N'")
extra_chese = input("do you want extra chese ? 'y' , 'N' ")
bill = 0
if size == 's':
    bill+=15
elif size =='m':
    bill+=20
else :
    bill+=25

if add_pepperoni == 'y':
    if size== 's':
        bill+=2
    else:
        bill+=3
if extra_chese == 'y':
    bill+=1
print(f"your final bill is ${bill}")

#Love calculator
print("wellcome to the love calculator")
name1= input("what is your name \n")
name2=input("what is their name \n")
combined_string= name1 + name2
lowe_case_string=combined_string.lower()

t=lowe_case_string.count("t")
r=lowe_case_string.count("r")
u=lowe_case_string.count("u")
e=lowe_case_string.count("e")
true = t+r+u+e
l=lowe_case_string.count("l")
o=lowe_case_string.count("o")
v=lowe_case_string.count("v")
e=lowe_case_string.count("e")
love = l+o+v+e

love_score1 =str( true)+str( love )
print(love_score1)
love_score=int(love_score1)

if love_score < 10 or love_score > 90:
    print(f"your love score is {love_score} . ")
elif (love_score >= 40) and (love_score<=50):
    print("you will stay togther ")
else:
    print(f"your love score is {love_score}")





