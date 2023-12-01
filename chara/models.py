from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

class  Category(models.Model):
    title = models.CharField(
        verbose_name='キャラ一覧',
        max_length=20)
    
    def __str__(self):
        return self.title

class CharaMake(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete = models.CASCADE
        )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
        )
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
        )
    comment = models.TextField(
        verbose_name='コメント',
        )
    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to = 'charas',
        )
    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to='charas',
        blank=True,
        null=True
        )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
        )
    
    def __str__(self):
        return self.title
    
