from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=20, required=True, error_messages={
                           'required': '用户不能为空', 'invalid': '格式错误'}, label="用户名", label_suffix=':', widget=forms.TextInput(attrs={'class': 'f', 'placeholder': "please input name"}))
    password = forms.CharField(max_length=20, required=True, error_messages={
                               'required': '密码不能为空', 'invalid': '格式错误'}, label="密码", label_suffix=":", widget=forms.PasswordInput(attrs={'class': 'f', 'placeholder': 'please input password'}))
    phone = forms.RegexField(required=True, regex="^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$", error_messages={
                             'required': "电话不能为空", 'invalid': '格式错误'}, label="电话", label_suffix=":", widget=forms.TextInput(attrs={'class': 'f', 'placeholder': 'please input your phone'}))
    email = forms.RegexField(required=True, regex="[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?", error_messages={
                             'required': "邮箱不能为空", 'invalid': '格式错误'}, label="电子邮件", label_suffix=":", widget=forms.TextInput(attrs={'class': 'f', 'placeholder': 'please input your e-mail'}))
    idNumber = forms.RegexField(regex="^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$", required=True, error_messages={
                                'required': "身份证不能为空", 'invalid': '格式错误'}, label="身份证号码", label_suffix=":", widget=forms.TextInput(attrs={'class': 'f', 'placeholder': 'please input your id number'}))
    country = forms.CharField(max_length=20, required=True, error_messages={
        'required': '不能为空', 'invalid': '格式错误'}, label="国家", label_suffix=":", widget=forms.TextInput(attrs={'class': 'f myCountry', 'placeholder': 'please input your country', 'id': 'myInput'}))
