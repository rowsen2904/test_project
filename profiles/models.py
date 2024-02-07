from datetime import timedelta
from uuid import uuid4

from django.contrib.auth.models import UserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class UserQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(is_active=True)


class UserManager(UserManager.from_queryset(UserQuerySet)):  # type: ignore
    def get_users_with_expired_referral(self):
        return self.filter(expiration_date__lte=timezone.now().date(), referral_code__isnull=False)


class User(AbstractUser):
    referral_code = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )
    expiration_date = models.DateField(null=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.id}. {self.username}"

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

    def __str__(self):
        return f'{self.inviter} - {self.invited}'
