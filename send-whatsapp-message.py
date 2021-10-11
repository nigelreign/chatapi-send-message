import requests

def send_message(phone_number, message):
    """
    Args:
        phone_number: user phone number
        message: message to user
    """
    instance = ""
    token = ""

    payload = {
        "phone": phone_number,
        "body": message
    }
    url = f" https://api.chat-api.com/{instance}/sendMessage?token={token}"
    response = requests.post(url=url, data=payload)

    """
        logger
    """
    if response:
        print("Whatsapp Response ",
                        {'code': 200, 'phoneNumber': phone_number, 'message': message})
    else:
        print("Whatsapp Response ",
                        {'code': 400, 'error': "Failed to send message"})


phone_number =  ""
message = "test message"
send_message(phone_number=phone_number, message=message)

