from django.core.mail import send_mail

__all__ = [
    'send_test',
]


def send_test():
    send_mail(
        'Subject',
        'Message',
        'fastcampus.2016@gmail.com',
        ['arcanelux@gmail.com']
    )
