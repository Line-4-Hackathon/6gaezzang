from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Blog
from .forms import BlogForm
from user.models import Fuser
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

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
    return render(request, 'detail.html', {'blog':blog})

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