#Create a tip calculator
bill1 = float(input("what is the amount of bill\n "))
tip = input("how much percent till you want to give:\n")
tip1 =int(tip)
cal_tip = (tip1/100)*bill1
total_bill = bill1 + cal_tip
divide = input("on how many persons you want to devide:\n ")
divide1 = int(divide)
each_bill = (round(total_bill/divide1, 3))
print(f"each person have to pay {each_bill}, in the bill ")