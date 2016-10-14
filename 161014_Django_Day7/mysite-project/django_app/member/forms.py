from django import forms


class SignupForm(forms.Form):
    # https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField()
    password2 = forms.CharField()
    last_name = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    nickname = forms.CharField(max_length=24)
    