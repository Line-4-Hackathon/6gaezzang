from django import forms
from .models import Fuser
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="아이디",
    error_messages={
        'required':"아이디를 입력하세요."
    })
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput,
    error_messages={
        'required':"비밀번호를 입력하세요."
    })

    def clean(self):
        clean_data = super().clean()
        username = clean_data.get('username')
        password = clean_data.get('password')

        try: 
            fuser = Fuser.objects.get(pk=username) 
            if not check_password(password, fuser.password): 
                self.add_error('password', '비밀번호가 틀렸습니다.') 
        except:  
            self.add_error('username', '가입하지 않은 아이디입니다.')

class SignupForm(forms.Form):
    username = forms.CharField(max_length=32, label="아이디",
    error_messages={
        'required':"아이디를 입력하세요."
    })
    password = forms.CharField(label="비밀번호", min_length=8, widget=forms.PasswordInput,
    error_messages={
        'required':"비밀번호를 입력하세요."
    })
    re_password = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput,
    error_messages={
        'required':"비밀번호를 한 번 더 입력하세요."
    })

    def clean(self):
        clean_data = super().clean()
        username = clean_data.get('username')
        password = clean_data.get('password')
        re_password = clean_data.get('re_password')

        if password != re_password :
            self.add_error('re_password', "비밀번호가 일치하지 않습니다.")
        try: 
            Fuser.objects.get(pk=username) 
            self.add_error('username', '이미 가입된 아이디입니다.') 
        except: 
            pass