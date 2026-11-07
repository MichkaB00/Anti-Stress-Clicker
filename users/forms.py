from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Ім'я", max_length=150)
    last_name = forms.CharField(label="Прізвище", max_length=150)

    error_messages = {
        "password_mismatch": "Паролі не збігаються.",
    }

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Логін"
        self.fields["password1"].label = "Пароль"
        self.fields["password2"].label = "Підтвердження пароля"
        self.fields["username"].error_messages["unique"] = (
            "Користувач із таким логіном уже існує."
        )
        self.fields["username"].help_text = ""
        self.fields["password1"].help_text = "Щонайменше 8 символів, не лише цифри."
        self.fields["password2"].help_text = ""
        self.order_fields(
            ["first_name", "last_name", "username", "password1", "password2"]
        )


class LoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "Неправильний логін або пароль.",
        "inactive": "Цей обліковий запис вимкнено.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Логін"
        self.fields["password"].label = "Пароль"


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")
        labels = {
            "first_name": "Ім'я",
            "last_name": "Прізвище",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
