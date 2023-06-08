from django.urls import path
from .views import Index, PostItem, CreatPost, EditPost, DeletePost
from django.shortcuts import redirect

urlpatterns = [
    path('index', Index.as_view(), name='index'),
    path('post/<int:pk>', PostItem.as_view()),
    path('', lambda request: redirect('index', permanent=False)),
    path('create_ad', CreatPost.as_view(), name='create_ad'),
    path('post/<int:pk>/edit', EditPost.as_view()),
    path('post/<int:pk>/delete', DeletePost.as_view()),

]
