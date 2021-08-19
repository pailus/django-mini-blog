from .serializer import *
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class CategoryViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
