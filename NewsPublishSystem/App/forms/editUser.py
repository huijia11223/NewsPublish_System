from django import forms


class EditUser(forms.Form):
    uid = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'disabled': 'false'}))
    username = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))   
    phone = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=20, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    country = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    idNumber = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'disabled': 'false'}))
