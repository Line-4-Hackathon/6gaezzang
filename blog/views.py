from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Blog
from .forms import BlogForm
from user.models import Fuser
from django.core.paginator import Paginator
from datetime import date, datetime, timedelta
import requests
from bs4 import BeautifulSoup

def loading(request):
    return render(request, 'loading.html')

def home(request):
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%93%B1%EC%82%B0'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    a_list = soup.select('ul.list_news > li.bx > div.news_wrap > div.news_area > a')
    title_list = []
    url_list = []
    num_list = [0,1,2,3,4,5]
    for num in range(0,6):
        url_list.append(a_list[num]['href'])
    for num in range(0, 6):
        title_list.append(a_list[num]['title'])
    
    return render(request, 'home.html',{'title_list':title_list,'url_list':url_list,'num_list':num_list})

# 첫 게시판 화면
def show(request):
    blog = Blog.objects.filter(is_del=0).order_by('-pub_date')
    paginator = Paginator(blog, 5)
    page = int(request.GET.get('p', 1))
    blogs = paginator.get_page(page)
    return render(request, 'show.html', {'blogs':blogs})

# 작성자, 날짜, 수정, 삭제 등등
def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    #session_cookie = request.session['user_id']
    user_id = request.session.get('user')
    user = Fuser.objects.get(pk=user_id)
    cookie_name = F'blog_hits:{user}'
    context = {
        'blog': blog,
    }
    response = render(request, 'detail.html', context)

    if request.COOKIES.get(cookie_name) is not None:
        cookies = request.COOKIES.get(cookie_name)
        cookies_list = cookies.split('|')
        if str(pk) not in cookies_list:
            response.set_cookie(cookie_name, cookies + f'|{pk}', expires=None)
            blog.hits += 1
            blog.save()
            return response
    else:
        response.set_cookie(cookie_name, pk, expires=None)
        blog.hits += 1
        blog.save()
        return response

    return render(request, 'detail.html', context)
   
    #return render(request, 'detail.html', {'blog':blog})

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form':form})

# 새 글 작성
def create(request):
    if request.method == "GET":
        form = BlogForm()
    elif request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            user_id = request.session.get('user')
            user = Fuser.objects.get(pk=user_id)
            pub_dated = timezone.now()
            new_blog = Blog(
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
                writer = user,
                pub_date = pub_dated,
            )
            new_blog.save()
            return redirect('show')
    return render(request, 'show.html', {'form':form})
    #return redirect('show', {'form':form})

def edit(request, pk):
    edit_blog = Blog.objects.get(id=pk)
    return render(request, 'edit.html', {'blog':edit_blog})

# 글 수정
def update(request, pk):
    update_blog = Blog.objects.get(id = pk)
    user_id = request.session.get('user')
    user = Fuser.objects.get(pk=user_id)
    update_blog.title = request.POST['title']
    update_blog.writer = user
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    #new_blog.image = request.FILES['image']
    update_blog.save()
    return redirect('detail', update_blog.id)

# 글 삭제
def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.is_del = 1
    delete_blog.delete()
    return redirect('show')