from django.urls import path
from .views import posts


app_name = 'apps.posts'


urlpatterns= [
    path('posts/', posts, name='posts'),
]