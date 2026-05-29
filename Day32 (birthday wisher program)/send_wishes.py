import smtplib
import datetime as dt
import random
my_email= "experimental.my2@gmail.com"
password= "1234$#@!"
now= dt.datetime.now()
weekday= now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes= quote_file.readlines()
        quote= random.choice(all_quotes)
    print(quote)
    with  smtplib.SMTP("smtp.gamil.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs= my_email,
                            msg=f"subject:Monday Motivation\n\n"
                                f"{quote}")