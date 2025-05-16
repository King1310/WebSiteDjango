from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
import re


from users.models import User


User = get_user_model()

class UserLoginForm(forms.Form):
    login_or_email = forms.CharField(label='Username or Email')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.user_cache = None

    def clean(self):
        cleaned_data = super().clean()
        login_or_email = cleaned_data.get('login_or_email')
        password = cleaned_data.get('password')

        if login_or_email and password:
            user = None
            if '@' in login_or_email:
                # Вводится email - ищем пользователя по email
                try:
                    user_obj = User.objects.get(email__iexact=login_or_email)
                    username = user_obj.get_username()
                    user = authenticate(self.request, username=username, password=password)
                except User.DoesNotExist:
                    user = None
            else:
                # Вводится username
                user = authenticate(self.request, username=login_or_email, password=password)

            if user is None:
                raise forms.ValidationError("Неверный логин/email или пароль.")
            else:
                self.user_cache = user

        return cleaned_data

    def get_user(self):
        return self.user_cache



class UserRegistrationForm(UserCreationForm):
    first = forms.CharField(required=True)
    last = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first",
            "last",
            "email",
            "password1",
            "password2",
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')

        if password:
            # Проверка на наличие заглавной буквы
            if not re.search(r'[A-Z]', password):
                self.add_error('password1', "Пароль должен содержать хотя бы одну заглавную букву.")
            # Проверка на наличие цифры
            if not re.search(r'\d', password):
                self.add_error('password1', "Пароль должен содержать хотя бы одну цифру.")
            # Проверка на наличие специального символа
            if not re.search(r'[\W_]', password):
                self.add_error('password1', "Пароль должен содержать хотя бы один специальный символ.")
            # Проверка на длину пароля
            if len(password) < 8:
                self.add_error('password1', "Пароль должен содержать не менее 8 символов.")

        return cleaned_data
