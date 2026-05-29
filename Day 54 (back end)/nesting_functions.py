import time


# def add(n1,n2):
#     return n1 +n2
#
# def subtract(n1,n2):
#     return n1 - n2
# def multiply(n1,n2):
#     return n1 * n2
#
# def divide(n1,n2):
#     return n1/n2
#
# #functions are First-class objects, can be passed around as arguments e.g. int/string/float etc
#
# def calculate(calc_function, n1,n2):
#     return calc_function(n1,n2)
#
# ans= calculate(divide, 6,3)
# print(ans)

#Nested Functions

# def outer_function():
#     print("i am outer")
#
#     def nested_function():
#         print(" i am inner ")
# outer_function()

#Functions can be returned from other functions
# def outer_function():
#     print("i am outer")
#
#     def nested_function():
#         print(" i am inner ")
#
#     return nested_function
# inner_function= outer_function()
# inner_function()

## Python Decorator function

def decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        #do something before
        function()
        #do something after
    return wrapper_function
@decorator_function
def say_hello():
    print("hello")
@decorator_function
def say_hi():
    print("hi")
def say_bye():
    print("bye")
say_hi()
say_bye()
say_hello()