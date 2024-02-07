from typing import Any, Dict, List


def get_referrals(inviter) -> List[Dict[str, Any]]:
    qs = inviter.referrals.all()
    data = []
    for x in qs:
        model = {
            "id": x.invited.id,
            "username": x.invited.username,
            "email": x.invited.email,
            "first_name": x.invited.first_name,
            "last_name": x.invited.last_name,
            "referral_code": x.invited.referral_code,
            "referrals_count": x.invited.referrals_count
        }
        data.append(model)

    return data
