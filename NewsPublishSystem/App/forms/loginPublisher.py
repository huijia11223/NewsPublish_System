from django import forms


class LoginPublisher(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'login', 'required':'True'}))
    passwd = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'passwd','required':'True'}))
