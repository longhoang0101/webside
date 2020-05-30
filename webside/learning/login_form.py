from django.contrib.auth.forms import AuthenticationForm
from django import forms





class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Tài khoản", max_length=8,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Mật khẩu", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
))

class RegisterForm(forms.Form):
    customer_name = forms.CharField(label="Tên hiển thị:", max_length=127)
    username = forms.CharField(label="Tài khoản:", max_length=8,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    customer_mail = forms.CharField(label="Email:", max_length=8,
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'customer_mail'}))
    password = forms.CharField(label="Mật khẩu", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

    password_again = forms.CharField(label="Nhập lại mật khẩu", max_length=30,
                                     widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

