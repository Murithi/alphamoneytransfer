import twilio
import twilio.rest
from django.conf import settings
from django.core.mail import send_mail

def send_twilio_message(to_number, body):
        client = twilio.rest.TwilioRestClient(
            settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        return client.messages.create(
            body=body,
            to=to_number,
            from_=settings.TWILIO_PHONE_NUMBER
        )

def this_send_email(username, key, email):
    email_subject = 'Account confirmation'
    email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/accounts/confirm/%s" % (username, key)
    send_mail(email_subject,
              email_body,
              'ericinoti@gmail.com',
              [email],
              fail_silently=False)
