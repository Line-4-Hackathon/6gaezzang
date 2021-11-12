from django.db import models
from user.models import Fuser

# Create your models here.
class Post(models.Model):
    writer = models.ForeignKey(Fuser, related_name="community", on_delete=models.CASCADE, verbose_name="작성자", null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.ManyToManyField(Fuser, related_name='likes', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="글작성일", null=True)
    top_fixed = models.BooleanField(verbose_name='상단고정', default=False)

    def __str__(self):
        return self.title