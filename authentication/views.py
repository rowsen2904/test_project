from rest_framework import generics

from .serializers import RegisterSerializer
from profiles.models import User


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        user = super().post(request, *args, **kwargs)
        referral_code = request.data.get("referral_code")
        if referral_code is not None:
            try:
                inviter = User.objects.get(referral_code=referral_code)
                invited = User.objects.get(username=user.data.get("username"))
            except User.DoesNotExist:
                pass
            else:
                inviter.set_new_referral(invited)

        return user
