from django.urls import path

from . import views

urlpatterns = [
    path(
        'create-referral-code/',
        views.CreateReferralCodeAPIView.as_view(),
        name='create-referral-code'
    )
]
