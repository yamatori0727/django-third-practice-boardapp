from django.db import models


class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    sns_image = models.ImageField(upload_to='', null=True, blank=True)
    good = models.IntegerField(null=True, blank=True, default=1)  # 投稿、データがからのものを受け付ける。
    read = models.IntegerField(null=True, blank=True, default=1)
    readtext = models.TextField(null=True, blank=True, default="a")
