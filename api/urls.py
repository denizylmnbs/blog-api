from django.urls import path
from .views import BlogPostCreate

urlpatterns = [
    path("blogs", BlogPostCreate.as_view(), name = "blog-post-create")
]
