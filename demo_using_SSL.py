import os
import smtplib

mail_username = os.environ.get("Email_user")
mail_password = os.environ.get("Email_pass")
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as smtp:

        smtp.login(mail_username, mail_password)
        recipients = ["sakhawathsust@gmail.com"]
        subject = "Experimental message"
        body = "Hello, it's my first Email using Python."
        message = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(mail_username, recipients,message)
except Exception as error:
    print("failed to run", error)

