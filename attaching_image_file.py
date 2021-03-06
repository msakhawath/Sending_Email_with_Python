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

images = ["pic.jpg", "pic1.jpg"]
for files in images:
    with open(files,"rb") as file:
        file_data = file.read()
        file_type = imghdr.what(file.name) # Delete this line to attach a pdf file.

        file_name = file.name  # if file_name not used image name won't show up in the attachment.
    msg.add_attachment(file_data,maintype = "image",subtype = file_type,filename =file_name)  # To attach a pdf file just change maintype to "application"
                                                                                              # and subtype to "octet-stream" and delete file_type line from above.
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as smtp:
        smtp.login(mail_username, mail_password)
        smtp.send_message(msg)

except Exception as error:
    print("failed to run", error)
