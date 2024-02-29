import logging

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
