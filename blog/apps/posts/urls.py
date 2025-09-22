from django.urls import path
from .views import *
from . import views



app_name = 'apps.posts'


urlpatterns= [
    path('posts/', PostListView.as_view(), name='posts'),
    path("posts/<int:id>/", PostDetailView.as_view(), name="post_individual"),
    path('post/', PostCreateView.as_view(), name='crear_post'),
    path('post/categoria/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('post/<int:pk>/modificar/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_delete'),
]