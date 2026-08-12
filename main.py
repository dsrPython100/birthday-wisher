import pandas
import smtplib
import datetime as dt
import random
import os

#MY SOLUTION WILL PICK UP MULTIPLE PEOPLE WHO HAVE THE SAME BIRTHDAY, ANGELA'S WONT

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

# 2. Check if today matches a birthday in the 2birthdays.csv
today = dt.datetime.now()
month = today.month
day_of_the_month = today.day

birthdays_dataframe = pandas.read_csv("birthdays.csv") #convert the csv into a dataframe so you can access rows and columns

for (index, row) in birthdays_dataframe.iterrows(): #go through each row and look at the column value
    if month == row["month"] and day_of_the_month == row["day"]:  #always use ___["___"]
        birthday_name = row["name"]
        birthday_email = row["email"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from 2birthdays.csv
        random_number = random.randint(1, 3)
        with open(f"./letter_templates/letter_{random_number}.txt") as send_letter:
            letter_contents = send_letter.read()
            mail_letter = letter_contents.replace("[NAME]", birthday_name)

        # 4. Send the letter generated in step 3 to that person's email address.
        #the below needs to be inside the if block
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # way to connect to our email providers smtp email server
            connection.starttls()  # transport layer security, secures connection to email server (encrypts it)
            connection.login(user=my_email, password=password)  # login to your email provider
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_email,
                msg=f"Subject: Happy Birthday!!\n\n{mail_letter}"
            )
