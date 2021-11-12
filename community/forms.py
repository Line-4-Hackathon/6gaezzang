from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(error_messages = {'required':"내용을 입력해주세요."}, label = "내용", widget = forms.Textarea)

    class Meta:
        model = Post
        fields = ['title', 'content',]
    
