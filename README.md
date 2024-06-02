# Email Notification Script

This repository contains a Python script to send an email notification using Gmail's SMTP server. The email content is generated from an HTML template, allowing for dynamic customization.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3 installed on your system.
- Necessary libraries: `smtplib`, `email`, `string`, and `pathlib`.

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/email-notification-script.git
   cd email-notification-script
   ```

2. **Install required libraries:**

   The required libraries are part of Python's standard library, so no additional installation is needed.

3. **Create an HTML template:**

   Create a file named `index.html` in the same directory with the following content:

   ```html
   <html>
   <body>
       <h1>Hello, ${name}!</h1>
       <p>This is a notification from your home.</p>
   </body>
   </html>
   ```

4. **Configure your email credentials:**

   Update the script with your email details:
   - Replace `"receiver email"` with the recipient's email address.
   - Replace `"sender email"` with your Gmail address.
   - Replace `"generated password"` with your Gmail App Password.

   > **Note:** For security reasons, it's recommended to use an App Password instead of your regular Gmail password. You can generate an App Password from your Google Account settings.

## Usage

Run the script using Python:

```sh
python send_email.py
```

## Script Overview

Here's a brief explanation of the script:

```python
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Create the email object
email = EmailMessage()

# Load and parse the HTML template
html = Template(Path("index.html").read_text())

# Set the email details
email["from"] = "Adrian"
email["to"] = "receiver email"
email["subject"] = "Notification from home"

# Substitute variables in the HTML and set the email content
email.set_content(html.substitute({"name" : "Caca"}), "html")

# Connect to the SMTP server and send the email
with smtplib.SMTP(host = "smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("sender email", "generated password")
    smtp.send_message(email)
    print("Email Sent")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to open an issue if you have any questions or suggestions. Contributions are welcome!

**Happy Coding!**

Adrian
