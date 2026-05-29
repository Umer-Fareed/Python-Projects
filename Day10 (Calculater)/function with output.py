#Functions with outputs


def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name= l_name.title()
    return f"{formated_f_name} {formated_l_name}"
result = format_name('fareed', 'uamr')
print(result)

"""#multiple return values
def format_name(f_name,l_name):

    take a first name last name and format it to return the tilte
    case verion of the name.

    if f_name == "" or l_name == "":
        return " you didn't provide a valid name"
    formated_f_name = f_name.title()
    formated_l_name= l_name.title()
    return f"{formated_f_name} {formated_l_name}"
print(format_name(input("what is your first name"),
                  input("what is your last name ")))
format_name()"""

#Days in a month of any year
def is_leap(year):
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def Days_in_month(year, month):
    if month > 12 or month < 1 :
        return "invalid month"
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month == 2:
        return 29
    else:
        # for days in month_days:
        #     day = month_days[month+1]
        # return day
        return month_days[month + 1]


year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
days = Days_in_month(year, month)
print(days)




