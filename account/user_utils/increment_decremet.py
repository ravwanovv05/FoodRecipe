from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


def increment(from_user, to_user):
    user_1 = User.objects.get(Q(pk=from_user))
    user_2 = User.objects.get(Q(pk=to_user))
    print(user_1.following)
    try:
        user_1.following += 1
        user_2.followers += 1
        user_1.save()
        user_2.save()
    except User.DoesNotExist:
        return False
    return True


def decrement(from_user, to_user):
    user_1 = User.objects.get(Q(pk=from_user))
    user_2 = User.objects.get(Q(pk=to_user))
    print(user_1.following)
    try:
        user_1.following -= 1
        user_2.followers -= 1
        user_1.save()
        user_2.save()
    except User.DoesNotExist:
        return False
    return True
