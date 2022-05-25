from re import A
import django


from django.urls import path
from blog.api.viewsets import(
                            ArricalesDetailView,
                            ArticalesLestView
                        )

urlpatterns = [
    path("article/",ArticalesLestView.as_view(),name="aricle_list"),
    path("article_detail/<int:pk>",ArricalesDetailView.as_view(),name="aricle_detail")
]