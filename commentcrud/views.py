from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from community.models import Post
from commentcrud.models import Comment
from user.models import Fuser

# Create your views here.
def commentcreate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            user_id = request.session.get('user')
            user = Fuser.objects.get(pk=user_id)
            comment.writer = user
            comment.post = post
            comment.save()
            return redirect('postshow', post_id=post.pk)
        else:
            redirect('list')
    else:
        form = CommentForm()
        return render(request, 'postshow.html', {'form':form, 'post':post})

def commentupdate(request, comment_id, post_id):
    comment = Comment.objects.get(id=comment_id)
    form = CommentForm(instance=comment)
    if request.method == "POST":
        update_form = CommentForm(request.POST, instance=comment)
        if update_form.is_valid():
            update_form.save()
            return redirect('postshow', post_id)
    return render(request, 'comment_update.html', {'form':form})

def commentdelete(request, comment_id, post_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('postshow', post_id)