from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UsernameField, UserCreationForm

UserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
        field_classes = {
            'username': UsernameField,
            }
