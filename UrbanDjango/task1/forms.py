# forms.py
from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(
        max_length=30,
        label='Введите логин',
        widget=forms.TextInput(attrs={'id': 'username', 'required': 'required'})
    )
    password = forms.CharField(
        min_length=8,
        label='Введите пароль',
        widget=forms.PasswordInput(attrs={'id': 'password', 'required': 'required'})
    )
    repeat_password = forms.CharField(
        min_length=8,
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'id': 'repeat_password', 'required': 'required'})
    )
    age = forms.IntegerField(
        label='Введите свой возраст',
        max_value=120,
        min_value=0,
        widget=forms.NumberInput(attrs={'id': 'age', 'required': 'required'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        if password and repeat_password and password != repeat_password:
            self.add_error('repeat_password', 'пароли не совпадают')