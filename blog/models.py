from django.db import models
from django.contrib.auth import get_user_model
from rest_framework import serializers

class Article (models.Model):
    title =models.CharField(max_length=200)
    blog_text=models.TextField(max_length=1000)
    author= models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    # author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    date=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    published=models.BooleanField()

    def __str__(self):

        return self.title

    