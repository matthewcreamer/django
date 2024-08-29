from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Owner, User

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Owner.objects.get(username=username)
        except Owner.DoesNotExist:
            try:
                user = User.objects.get(username=username)
                print('no owner', username, user)
            except User.DoesNotExist:
                print('no users')
                return None
        if user and check_password(password, user.password):
            return user
        return None

    def get_user(self, user_id):
        try:
            user = Owner.objects.get(pk=user_id)
            return user
        except Owner.DoesNotExist:
            try:
                user = User.objects.get(pk=user_id)
                return user
            except User.DoesNotExist:
                return None