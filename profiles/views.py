from django.conf import settings
from django.core.mail import send_mail
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CreateReferralCodeAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        referral_code = request.user.create_new_referral_code()
        sender = settings.EMAIL_HOST_USER
        send_mail(
            'New Referral Code',
            f'Your new referral code is: {referral_code}',
            sender,
            ["bayrumovw@gmail.com"],
            fail_silently=False
        )
        return Response({'referral_code': referral_code}, status=200)
