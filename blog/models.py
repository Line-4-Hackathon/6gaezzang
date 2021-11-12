from django.db import models
from user.models import Fuser

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='글 제목')
    writer = models.ForeignKey(Fuser, verbose_name = "작성자", on_delete = models.CASCADE, null=True, default="")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    is_del = models.BooleanField(default=False)
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')
    body = models.TextField(verbose_name = "내용")
    image = models.ImageField(upload_to = "blog/", blank=True, null=True, verbose_name = "사진")

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]