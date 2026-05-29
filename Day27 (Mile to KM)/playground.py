def add(*args):
     ans= 0
     for n in args:
         ans+=n
     print(ans)

add(3,4,5,6,7)

# def calculate(n, **kwargs):
#     print(**kwargs)
#     n+=kwargs["add"]
#     n*=kwargs["multiply"]
#
#
#
#
#
# calculate(2, add= 3, multiply= 5)

class Car:

    def __init__(self, **kw):
        self.make= kw["make"]
        self.model= kw["model"]
car = Car(make= "blue")
print(car)