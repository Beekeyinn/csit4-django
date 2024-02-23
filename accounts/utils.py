from profiles.models import UserProfile


def create_profile(user):
    UserProfile.objects.get_or_create(user=user)
