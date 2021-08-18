
from django.db import models
from django.contrib.auth.models import User
from master.models import Category, Tag

class Post(models.Model):
    judul = models.CharField(max_length=500)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    feature_image = models.ImageField(upload_to='uploads/')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.judul



class Comment(models.Model):
    nama = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nama