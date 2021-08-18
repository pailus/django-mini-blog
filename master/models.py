from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    nama = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.nama 

    class Meta:
        ordering = ['id']


class Tag(models.Model):
    nama = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.nama 
        
    class Meta:
        ordering = ['id']