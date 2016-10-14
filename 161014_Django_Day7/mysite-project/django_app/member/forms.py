from django import forms


class SignupForm(forms.Form):
    # https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/
    email = forms.EmailField(max_length=100)
    # 나머지 요소 작성해보세요