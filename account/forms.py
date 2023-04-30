from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    # username , password 1 , password 2를 기본적으로 입력 받는다.
    # 추가적으로 email을 받을 것인데, 기본값은 아니기에 수동으로 잡아줘야함.
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")