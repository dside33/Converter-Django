from user_profile.models import UserProfile


def get_user_profile(request):
    profile = None
    if request.user.is_authenticated:
        profile = UserProfile.objects.filter(user=request.user).first()

    return {'user_profile': profile}