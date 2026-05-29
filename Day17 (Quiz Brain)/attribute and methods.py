

Class Car:
    def __init__(self,seats):
        self.seat = seats                 #initialise attributes
        0e8712

    #methods inside class
    def enter_car_mode():
        self.seats = 2

# class User:
#     #attributes
#     def __init__(self, user_id,username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#     #methods
#     def follow(self, user):
#         user.followers+=1
#         self.following+=1
# user_1 = User("001","umar")
# user_2 = User("002","adeel")
# print(user_1.followers)
#
# user_1.follow(user_2)
# print(user_1.following)
# print(user_1.followers)
# print(user_2.following)
# print(user_2.followers)

#Create a student class that takes name &marks of 3 subjects as arguments
#in constructor then create a method to print the average.

# class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print("hello boys ")
    def avg(self):
        total_marks =0
        for mark in self.marks:
             total_marks += mark
             avg = round(total_marks/len(self.marks))
        return avg
s1 = Student("fared",[34,54,65])
print(s1.avg())


# class Account :
#     def __init__(self, balance, account_no):
#         self.balance =balance
#         self.account_no = account_no
#     def debit(self,amount):
#         self.balance+=amount
#         print(f"Rs. {amount} is debited")
#         print(f"total balance is {self.balance}")
#     def credit(self, amount):
#         self.balance-=amount
#         print(f"Rs. {amount} is credit")
#         print(f"total balance is {self.balance}")
#     def total_amount(self):
#         return self.balance
#
# account1 = Account(342,"123")
# account1.debit(20000)
