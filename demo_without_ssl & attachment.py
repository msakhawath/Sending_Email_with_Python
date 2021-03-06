# Gmail requires that you connect to port 465 if using SMTP_SSL(),
# and to port 587 when using .starttls().
# Secure socket layer and Transport Layer Security.
# you can also use getpass module not to display the password
# IMPORTANT ATTENTION######################################

# Must form an app password after using two factor authentication.
# Use that app password in the environ variable. Otherwise programme won't run


# Using ehlo() and starttls() method and not using SSL


import os
import smtplib

mail_username = os.environ.get("Email_user")
mail_password = os.environ.get("Email_pass")
try:
    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()           # Identify us with the mail server that we are using.
        smtp.starttls()       # To encrypt the message
        smtp.ehlo()           # Re identify again as encrypted message
        smtp.login(mail_username, mail_password)
        recipients = ["sakhawathsust@gmail.com","niharaminur@gmail.com"]
        subject = "Experimental message"
        body = "Hello, it's my first Email using Python."
        message = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(mail_username, recipients,message)
except Exception as error:
    print("failed to run", error)















