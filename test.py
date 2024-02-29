import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger(__name__)
import requests
from decouple import config

def send_notification(recipient, message):
    logger.warning(recipient)
    apiKey = config("SMS_KEY")
    endPoint = "https://api.mnotify.com/api/sms/quick"
    data = {
        "recipient[]": [recipient],
        "sender": config("SENDER"),
        "message": message,
        "is_schedule": False,
        "schedule_date": "",
    }
    url = endPoint + "?key=" + apiKey
    response = requests.post(url, data)
    data = response.json()
    return data




def send_email(receiver_email, body):
    sender_email = config("SENDER_MAIL")
    password = config("PASSWORD")
    subject = "Budget Breakdown For The Month"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach body
    message.attach(MIMEText(body, "plain"))

    # Establish a secure connection with the SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:  
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully")


