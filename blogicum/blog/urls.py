from django.urls import path
from .views import index, post_detail, category_posts

urlpatterns = [
    path('', index, name='blog_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', category_posts, name='category_posts'),
]
