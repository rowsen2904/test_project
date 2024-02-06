from django.conf import settings
from django.core.mail import send_mail
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.tasks import send_email


class CreateReferralCodeAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, )
    email_subject = 'New Referral Code'
    from_email = settings.EMAIL_HOST_USER

    def get(self, request, *args, **kwargs):
        referral_code = request.user.create_new_referral_code()
        send_email.delay(
            subject=self.email_subject,
            message=f'Your new referral code is: {referral_code}',
            from_email=self.from_email,
            recipient_list=[request.user.email]
        )
        return Response({'referral_code': referral_code}, status=200)
