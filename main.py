import smtplib
import os

RECIPIENTS = ["ratter.outwork_2h@icloud.com", "vgl0911@icloud.com"]
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")


response = requests.get(url="https://zenquotes.io/api/random")  # paste the URL as a STRING
response.raise_for_status()
data = response.json()

author = data[0]["a"]   #FORMAT IS A LIST WITH DICTIONARIES, NEED TO GET LIST POS THEN DICT KEY
quote = data[0]["q"]

with smtplib.SMTP("smtp.gmail.com",
                  port=587) as connection:  # way to connect to our email providers smtp email server
    connection.starttls()  # transport layer security, secures connection to email server (encrypts it)
    connection.login(user=my_email, password=password)  # login to your email provider
    for address in RECIPIENTS:
        connection.sendmail(
            from_addr=my_email,
            to_addrs=address,
            msg=f"Subject: Your Daily Zen\n\n{quote}\n-- {author}"
