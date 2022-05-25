from django.db import models
from django.contrib.auth import get_user_model

class Article (models.Model):
    title =models.CharField(max_length=200)
    blog_text=models.TextField()
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    