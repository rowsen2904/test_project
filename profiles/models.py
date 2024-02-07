from datetime import timedelta
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    referral_code = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )
    expiration_date = models.DateField(null=True)

    @property
    def referrals_count(self):
        return self.referrals.count()

    def set_new_referral(self, referral):
        return self.referrals.create(invited=referral)

    def create_new_referral_code(self):
        self.referral_code = uuid4().hex
        self.expiration_date = (timezone.now() + timedelta(days=10)).date()
        self.save()
        return self.referral_code

    def delete_referral_code(self):
        self.referral_code = None
        self.expiration_date = None
        self.save()
        return self.referral_code


class Referral(models.Model):
    inviter = models.ForeignKey(
        User,
        related_name='referrals',
        on_delete=models.CASCADE
    )
    invited = models.OneToOneField(
        User,
        related_name='referral',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
