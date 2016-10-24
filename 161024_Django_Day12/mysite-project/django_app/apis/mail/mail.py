from django.core.mail import send_mail
from django.conf import settings
__all__ = [
    'send_test',
]
def send_test():
    send_mail(
        'Subject',
        'Message',
        settings.EMAIL_HOST_USER,
        ['arcanelux@gmail.com']
    )

