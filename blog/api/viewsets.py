from rest_framework.generics import (
                                        ListAPIView,
                                        RetrieveUpdateDestroyAPIView,
                                        RetrieveUpdateAPIView,
                                        ListCreateAPIView
                                    )
from blog.models import Article
from .serializers import ArticalSerializer
from .permissions import IsOwnerOrReadonly

class ArticalesLestView(ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticalSerializer
    

class ArricalesDetailView(RetrieveUpdateAPIView):
    queryset=Article.objects.all()        
    serializer_class=ArticalSerializer
    permission_classes=(IsOwnerOrReadonly, )