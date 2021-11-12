from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Fuser
from .forms import LoginForm, SignupForm
from django.contrib.auth import logout as auth_logout
from django.views.generic import FormView

# Create your views here.
"""
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})"""
"""
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')

    elif request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        re_password = request.POST.get("re_password", None)

        res_data = {} 

        if not (username and password and re_password) :
            res_data['error'] = "모든 칸을 입력해야 합니다."
        elif password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = "비밀번호가 다릅니다."
        else :
            fuser = Fuser(username=username, password=make_password(password),)
            fuser.save()
        return render(request, 'home.html', res_data)"""

class LoginView(FormView): 
    template_name = 'login.html' 
    form_class = LoginForm 
    success_url = '/' # 메인으로 
    
    def form_valid(self, form): 
        cleaned_data = form.cleaned_data 
        username = cleaned_data.get('username') # db에 저장되어 있는 email # Session객체-dictionary 형태:key-value쌍이 필요 # 로그인 -> session에 로그인 여부를 확인할 수 있는 체크값을 넣어둔다. 
        self.request.session['user'] = username # request: HttpRequest(사용자 HTTP 요청정보) 
        return super().form_valid(form)

class JoinView(FormView): 
    template_name = 'signup.html' 
    form_class = SignupForm 
    success_url = '/' 
    
    def form_valid(self, form): 
        cleaned_data = form.cleaned_data # dictionary  
        password = make_password(cleaned_data.get('password')) # 암호화 처리 
        username = cleaned_data.get('username') 
     
        fuser = Fuser(password=password, username=username) 
        fuser.save() 
        return super().form_valid(form)

def logout(request):
    auth_logout(request)
    return redirect('home')