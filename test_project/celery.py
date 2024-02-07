"""Celery tasks."""

from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

from test_project.settings import TIME_ZONE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")
app = Celery("test_project", include=['core.tasks'])

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_schedule = {
    # Every day
    "delete_expired_referrals": {
        "task": "core.tasks.delete_expired_referral_codes",
        "schedule": crontab(hour=0),
    },
}

app.conf.timezone = TIME_ZONE
