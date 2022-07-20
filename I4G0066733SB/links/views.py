from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializer import LinkSerializer
from links.models import Link

class PostListApi(GenericAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(GenericAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    

class PostDetailApi(GenericAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(GenericAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(GenericAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer



