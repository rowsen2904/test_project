from django.db import models
from django.http import Http404


def get_object_from_qs_or_404(qs: models.QuerySet, **kwargs):
    try:
        return qs.get(**kwargs)
    except qs.model.DoesNotExist as exc:
        raise Http404 from exc
