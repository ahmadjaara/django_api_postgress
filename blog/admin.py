from django.contrib import admin
from .models import Article

# Register your models here.

class AdminArticle(admin.ModelAdmin):
    list_display=["title","author","published"]

admin.site.register(Article,AdminArticle)