from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields = UserCreationForm.Meta.fields


