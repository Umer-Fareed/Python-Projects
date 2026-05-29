import smtplib
import datetime as dt

my_email = "experimental.my2@gmail.com"
password= "zvmj ajug fthq gzgh"


#Birthdat Wisher Project
##################### Normal Starting Project ######################

# 2. Check if today matches a birthday in the birthdays.csv
today= (dt.datetime.now().month,dt.datetime.now().day )

# HINT 2: Use pandas to read the birthdays.csv
import pandas
data= pandas.read_csv("birthdays.csv")
#Dictionary comprehension
birthday_dict = {(data_row.month,data_row.day): data_row for (index, data_row) in data.iterrows()}

print(birthday_dict)
import random
if today in birthday_dict:
    birthday_person= birthday_dict[today]
    file_path= f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents= letter_file.read()
        contents= contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs= birthday_person["email"],
            msg= f"subject: Heppy Birthday \n\n"
                 f"{contents} " )
