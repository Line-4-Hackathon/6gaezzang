from django.db import models
from community.models import Post
from user.models import Fuser
# Create your models here.

class Comment(models.Model):
    writer = models.ForeignKey(Fuser, related_name="comment", on_delete=models.CASCADE, verbose_name="댓글작성자", null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content