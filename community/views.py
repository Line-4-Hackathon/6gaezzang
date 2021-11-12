from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import PostForm
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator
from user.models import Fuser

def list(request):
    posts = Post.objects.order_by('-pub_date')
    notice_fixed = Post.objects.filter(top_fixed=True).order_by('-pub_date')
    page = request.GET.get('page','1')
    paginator = Paginator(posts, 10)
    page_obj = paginator.page(page)
    return render(request, 'list.html', {'posts': page_obj})

def postshow(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'postshow.html', {'post': post})

def notice1(request):
    return render(request, 'notice1.html')

def notice2(request):
    return render(request, 'notice2.html')

def postnew(request):
    if request.user.is_authenticated: 
        return render(request, 'postnew.html')

def postcreate(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():            
            post = form.save(commit=True)
            user_id = request.session.get('user')
            user = Fuser.objects.get(pk=user_id)
            post.writer = user
            post.save()
            return redirect('list')
        else:
            form = PostForm()
            messages.warning(request,'본문 내용을 작성해주세요')
            return render(request, 'new.html', {'form':form}) 
    else:
        form = PostForm()
        messages.info(request,'태그는 쉼표로 구분해주세요. ex)일인분,레시피')
        return render(request, 'postnew.html', {'form':form})  

def postedit(request):
    return render(request, 'postedit.html')

def postupdate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('postshow', post_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'postedit.html', {'form':form})

def postdelete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('list')

def likes(request, post_id): 
    post = get_object_or_404(Post, pk=post_id)
    post.like.add(request.username)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))