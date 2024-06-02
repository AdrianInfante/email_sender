
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # Help us to access to the html file

email = EmailMessage() #creates the email object
html = Template(Path("index.html").read_text()) # Path become a Template Object

email["from"] = "Adrian"
email["to"] = "receiver email"
email["subject"] = "Notification from home"

email.set_content(html.substitute({"name" : "Caca"}), "html")

with smtplib.SMTP(host = "smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("sender email", "generated password")
    smtp.send_message(email)
    print("Email Sent")
