from typing import List

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email(subject: str, message: str, from_email: str, recipient_list: List[str]) -> None:
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list
    )
    print("Email sent!")
