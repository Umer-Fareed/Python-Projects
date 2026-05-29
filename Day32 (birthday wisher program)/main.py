import smtplib

email= "experimental.my2@gmail.com"
password= "zvmj ajug fthq gzgh"
connection = smtplib.SMTP("smtp.gmail.com", 587)

connection.starttls()
connection.login(user=email , password= password)
connection.sendmail(from_addr=email,
                    to_addrs="experimental.my2@yahoo.com",
                    msg="subject:Hello\n\n hi my name is umer and i am writting an email")
connection.close()



























