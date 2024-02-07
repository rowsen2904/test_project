from django.urls import path

from . import views

urlpatterns = [
    path(
        'referral-code/',
        views.ReferralCodeAPIView.as_view(),
        name='referral-code'
    ),
    path('my-referrals/', views.MyReferralsAPIView.as_view(), name='my-referrals')
]
