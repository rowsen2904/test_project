from typing import List

from celery import shared_task
from django.core.mail import send_mail

from profiles.models import User


@shared_task
def send_email(subject: str, message: str, from_email: str, recipient_list: List[str]) -> str:
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list
    )
    return "Message sent to mail."


@shared_task
def delete_expired_referral_codes() -> str:
    qs = User.objects.get_users_with_expired_referral()
    for x in qs:
        x.delete_referral_code()

    return "Expired referral codes has been deleted!"
