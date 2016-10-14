from django import forms


class SignupForm(forms.Form):
    # https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/
    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    last_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    first_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    nickname = forms.CharField(
        max_length=24,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
