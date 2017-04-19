from django import forms
from django.conf import settings
from django.db.models import Q
from .models import User,Event
import re

class CommentForm(forms.Form):

    author = forms.CharField(widget=forms.TextInput(attrs={
                                                           'id':'author','class':'comment_input',
                                                           'required':'required','size':'25',
                                                           'tabindex':'1'}),
                                                           max_length=50,
                                                           error_messages={'required':u"username不能为空"})
    email = forms.EmailField(widget=forms.TextInput(attrs={'id':'email','type':'email',
                                                           'class':'comment_input','required':'required',
                                                           'size':'25','tabindex':'2'}),
                                                           max_length=50,
                                                           error_messages={'required':"email不能为空"})
    jobnum = forms.CharField(widget=forms.TextInput(attrs={'id':'jobnum',
                                                        'class':'comment_input','size':'25',
                                                        'tabindex':'3',}),
                                                        max_length=100,required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={'id':'commment','class':'message_input',
                                                           'required':'required','cols':'50','rows':'5',
                                                           'tabindex':'4',}),
                                                           error_messages={'required':"评论不能为空",})
                                                           

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
                                                     "placeholder":"用户名","required":'required',
                                                     "size":'25','tabindex':'1',}),
                                                      max_length='50',error_messages={'required':'用户名不能为空',})

    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                                      "placeholder":"请输入密码","required":'required',
                                                      "size":'25',"tabindex":'2',}),
                                                      max_length=20,error_messages={"required":"密码不能为空",})

class RegForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
                                                             "placeholder":"用户名","required":'required',
                                                             "size":'25','tabindex':'1',}),
                                                             max_length='50',error_messages={'required':'用户名不能为空',})
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                                                              "placeholder":"请输入密码","required":'required',
                                                              "size":'25',"tabindex":'2',}),
                                                              max_length=20,error_messages={"required":"密码不能为空",})
    jobnum = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"请输入工号",'size':'25',
                                                          'tabindex':'3',}),
                                                           max_length=100,required=False)

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'请输入邮箱地址','required':'required',
                                                         'size':'25','tabindex':'2'}),
                                                         max_length=50,
                                                         error_messages={'required':"email不能为空"})

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('username','jobnum','email','mobile','address','events','eventdetail')
        widgets = {
                'username':forms.TextInput(attrs={'size':'25','placeholder':'请输入您的姓名','tabindex':1,}),
                'jobnum':forms.TextInput(attrs={'size':'25','placeholder':'请输入您的工号','tabindex':2,}),
                'email':forms.TextInput(attrs={'size':'25','placeholder':'请输入您的邮箱','tabindex':3,}),
                'mobile':forms.TextInput(attrs={'size':'25','placeholder':'请输入您的电话','tabindex':4,}),
                'address':forms.TextInput(attrs={'size':'25','placeholder':'办工地址：楼号，层数，门派号','tabindex':5,}),
                'events':forms.Select(attrs={'tabindex':6,}),
                'eventdetail':forms.Textarea(attrs={'cols':'50','rows':'10','placeholder':'请简单描述问题','tabindex':6,}),
#                'grade':forms.Select(attrs={'tabindex':7,},),

        }
        
class GradeForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('grade','gradetext')
        widgets={
                'gradetext':forms.Textarea(attrs={'cols':'50','rows':'5','placeholder':'您的建议','tabindex':6,}),
        
        }


