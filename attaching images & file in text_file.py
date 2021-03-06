import os
import smtplib
from email.message import EmailMessage
import imghdr

mail_username = os.environ.get("Email_user")
mail_password = os.environ.get("Email_pass")
recipients = ["sakhawathsust@gmail.com"]
msg = EmailMessage()
msg["Subject"] = "Attaching two image.."
msg["From"] = mail_username
msg["To"] = recipients

with open("est.txt", "r") as text_file:
    file_data1 = text_file.read()
    msg.set_content(file_data1)

images = ["pic.jpg", "pic1.jpg"]
for image in images:
    with open(image,"rb") as image_file:
        file_data = image_file.read()
        file_type = imghdr.what(image_file.name)

        file_name = image_file.name

    msg.add_attachment(file_data, maintype ="image", subtype = file_type, filename =file_name)


try:
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as smtp:
        smtp.login(mail_username, mail_password)
        smtp.send_message(msg)

except Exception as error:
    print("failed to run", error)
