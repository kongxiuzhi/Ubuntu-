from django import forms
from .models import User

class RUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('job_number','name','first_name','last_name','passwd','email','is_staff')
        widgets = {'passwd':forms.PasswordInput}



class LUserForm(forms.Form):
    username = forms.CharField(label="用户名",max_length=30)
    password = forms.CharField(label="密码",max_length=128,widget=forms.PasswordInput)


