from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.

class BlogPostCreate(generics.CreateAPIView):
    queryset = BlogPost.objects.all().order_by("-created_at")
    model = BlogPost
    serializer_class = BlogPostSerializer