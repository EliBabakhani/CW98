from django import forms
from .models import CustomUser
from django.contrib.auth.hashers import make_password



class UserRegisterForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=CustomUser
        fields=('username', 'email', 'password')

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")
        return cleaned_data
    
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserLogInForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)