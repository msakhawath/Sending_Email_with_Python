# Important takeway: While using absolute path use r before the string.

import os
import smtplib
from email.message import EmailMessage

mail_username = os.environ.get("Email_user")
mail_password = os.environ.get("Email_pass")
recipients = ["sakhawathsust@gmail.com"]
msg = EmailMessage()
try:
    with open(r'C:\Users\sakha\PycharmProjects\Sending_Email\est.txt',"r",encoding="utf-8") as file:  # In the absolute path give your file path
        file_data = file.read()
        msg.set_content(file_data)
except Exception as e:
    print("Error", e)
msg["Subject"] = "Experimental message"
msg["From"] = mail_username
msg["To"] = recipients

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as smtp:
        smtp.login(mail_username, mail_password)
        smtp.send_message(msg)

except Exception as error:
    print("failed to run", error)
