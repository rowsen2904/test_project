from django.conf import settings
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from core.tasks import send_email
from helpers.shortcuts import get_object_from_qs_or_404
from helpers.utils import get_referrals


class ReferralCodeAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, )
    email_subject = 'Referral Code Information'
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

    def delete(self, request, *args, **kwargs):
        request.user.delete_referral_code()
        send_email.delay(
            subject=self.email_subject,
            message=f'Your referral code has been deleted.',
            from_email=self.from_email,
            recipient_list=[request.user.email]
        )
        return Response({'message': 'Referral code has been deleted'}, status=200)


class MyReferralsAPIView(GenericAPIView):
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        inviter_id = request.query_params.get('inviter_id')
        if inviter_id is not None:
            inviter = get_object_from_qs_or_404(self.queryset, pk=inviter_id)
            referrals = get_referrals(inviter)
            data = {
                "referrals_count": inviter.referrals_count,
                "referrals": referrals
            }
            return Response(data, status=200)

        return Response({"message": "No inviter id provided"}, status=400)
