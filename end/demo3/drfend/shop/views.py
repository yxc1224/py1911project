from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class CategoryViewSets(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class=CategorySerializer

class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerializer