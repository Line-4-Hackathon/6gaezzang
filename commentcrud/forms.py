from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='댓글을 입력해주세요', max_length=100)
    class Meta:
        model = Comment
        fields = ['content']