from django.db import models

# Create your models here.
class Fuser(models.Model):
    username = models.CharField(max_length=20, verbose_name="사용자 아이디", primary_key=True)
    password = models.CharField(max_length=20, verbose_name="비밀번호")

    def __str__(self): 
        return self.username

    class Meta:
        db_table = 'users'