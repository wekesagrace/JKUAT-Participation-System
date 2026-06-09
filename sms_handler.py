import africastalking
import urllib3
urllib3.disable_warnings()

def initialize_sms(username, api_key):
    africastalking.initialize(username, api_key)
    return africastalking.SMS

def send_acknowledgement(sms_service, phone_number):
    try:
        message = (
            "Thank you for your feedback! "
            "Your opinion has been received by SautiYetu. "
            "Your voice matters!"
        )
        sms_service.send(message, [phone_number])
        print(f"Acknowledgement sent to {phone_number}")
    except Exception as e:
        print(f"Note: Acknowledgement not sent — {str(e)}")