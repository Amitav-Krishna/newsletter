import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "python.testing.amitav@gmail.com"
receiver_email = "papadogspapa@gmail.com"
password = "LICJ SJXC RFQS XWMJ"

message = MIMEMultipart("alternative")

message["Subject"] = "Test HTML Email"
message["From"] = sender_email
message["To"] = receiver_email

with open('newsletter.html', 'r') as file:
    html_content = file.read()

part = MIMEText(html_content, "html")

message.attach(part)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message.as_string())
server.quit()

print("Email sent!")
