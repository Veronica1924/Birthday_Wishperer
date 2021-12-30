import pandas
import datetime as dt
import smtplib
import random

# <---------------------Defining variable ------------:

my_email = "veronica.moldovan@outlook.com"
password = "Welcome2020*"

file = pandas.read_csv("birthdays.csv")
data = file.to_dict(orient="records")

today = dt.datetime.now()

#<-----------------Sending conditions checking --------------:
for i in data:
    path = f"letter_templates/letter_{random.randint(1,4)}.txt"

    with open(path, mode="r") as file:
        quote1 = file.read()
        quote = quote1.replace("[NAME]", i["name"])

    if i["month"] == today.month and i["day"] == today.day:
        with smtplib.SMTP("outlook.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=i["email"],
                                msg=f"Subject: Monday Quote\n\n{quote}")
