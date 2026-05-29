#functions with inputs
def greeting(something):
    print(f"hello {something}")
    print("have a good day")
    print("have a bless day")

greeting("angela")

#function with more then one input
def greet_with(name , location ):
    print(f"hello { name }")
    print(f"what is the weather right there in {location }")

greet_with(location='lahore',name='ali')

#add two number
# def add(a,b):
#     c = a + b
#     print(c)
#
# add(4,5)

#wall paint
def wall_paint(height, width):
    covrage = 5
    area_cover = round((height *width) / covrage )
    return (area_cover)
height=int(input("enter the height of wall: "))
width = int(input("enter the width of wall: "))
result = wall_paint(height,width)
print(f"the number of cans you want to use are {result}")

#prime number check
def is_prime(number):
    if number == 0 or number == 1:
        print("it's a print number: ")
    elif number > 1:
        flag = False
        for i in range(2,number):
            if number%i==0:
                flag = True
            break
        if flag:
            print("number is not a print number ")
        else:
            print("number is  prime number ")

number = int(input("Enter the number : "))
is_prime(number)


