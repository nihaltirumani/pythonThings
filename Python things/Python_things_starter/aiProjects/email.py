import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "your_email@gmail.com"
sender_password = "your_email_password"

# Email content
subject = "Subject of the Email"
body = "Body of the Email"

# Email addresses
recipient_email = "recipient_email@example.com"

# SMTP configuration for Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Use TLS encryption
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
