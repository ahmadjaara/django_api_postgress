from rest_framework import serializers

from blog.models import Article

class ArticalSerializer(serializers.ModelSerializer):
    class Meta:
        fields=["title","blog_text","author","published"]
        # read_only_fields =["author"]
        # author = serializers.ReadOnlyField(source='Article.author')
        model =Article
    