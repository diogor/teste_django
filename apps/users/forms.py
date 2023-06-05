from .models import User
from django import forms

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmação de senha", widget=forms.PasswordInput)
    
    def clean_password2(self):
        if self.cleaned_data["password"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("As senhas não conferem")
        return self.cleaned_data["password2"]

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
