from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    referral_code = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )

    def create_new_referral_code(self):
        self.referral_code = uuid4().hex
        self.save()

    def get_count_of_referrals(self):
        print(self.referrals)


class Referral(models.Model):
    inviter = models.ForeignKey(
        User,
        related_name='referrals',
        on_delete=models.CASCADE
    )
    invited = models.OneToOneField(
        User,
        related_name='referral',
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
