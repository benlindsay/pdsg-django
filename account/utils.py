from .models import Profile

def get_or_create_profile(user):
    try:
        p = user.profile
    except:
        p = Profile(user=user)
        p.save()
    return p
