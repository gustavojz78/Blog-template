from django.urls import path
from .views import create_post, inicio, my_profile, posts_view, search_user

urlpatterns = [
    path('', inicio, name="index"), #Default view
    path('profile', my_profile, name="Profile"),
    path('posts', posts_view, name="Posts"),
    path('create-post', create_post, name="Create post"),
    path('search-user', search_user, name="Search user")
]