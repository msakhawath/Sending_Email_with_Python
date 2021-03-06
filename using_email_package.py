import os
import smtplib
from email.message import EmailMessage # email package very handy

mail_username = os.environ.get("Email_user")
mail_password = os.environ.get("Email_pass")
recipients = ["sakhawathsust@gmail.com"]
msg = EmailMessage()
msg["Subject"] = "Experimental message"
msg["From"] = mail_username
msg["To"] = recipients
msg.set_content("Another Message")
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as smtp:
        smtp.login(mail_username, mail_password)
        smtp.send_message(msg)

except Exception as error:
    print("failed to run", error)
