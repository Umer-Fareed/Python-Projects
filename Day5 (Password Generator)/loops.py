# loops
#simple loop
# fruits = ["apple ", " peach " , " pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

#total height
height = input("enter the list of students height ").split()
for n in range(0, len(height)):
    height[n] = int(height[n])
print(height)
avg = 0
for n in height:
    avg+=n
print(avg)
avg=avg/len(height)
print(f" the avg height of students is { avg }")

#heighest score
student_score = input("Input a list of student score").split()
for n in range(0 , len(student_score)):
    student_score[n]= int(student_score[n])
print(student_score)
heigh_score = 0
for n in student_score:
    if n > heigh_score:
        heigh_score = n
print(f"the heighest score for student is {heigh_score}")

#for loop with range
# total = 0
# for number in range(1 , 101):
#     total+=number
# print(total)

#total of evens
total = 0
for n in range(1 , 101):
    if n%2==0:
        total+=n
print(total)

#fizzbuzz

for n in range(1, 100 ):
    if n % 3 == 0 and n % 5 == 0 :
        print("bizzbuzz")
    elif n%5 == 0:
        print("buzz")
    elif n%3== 0 :
        print("fizz ")
    else:
        print(n)

