from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10, required=True, error_messages={
                               'required': '用户不能为空', 'invalid': '格式错误'}, label="用户名", label_suffix=":", widget=forms.TextInput(attrs={'class': 'user', 'placeholder': 'please input your name'}))
    password = forms.CharField(max_length=10, required=True, error_messages={
                               'required': '密码不能为空', 'invalid': '格式错误'}, label='密码', label_suffix=':', widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'please input your name'}))
