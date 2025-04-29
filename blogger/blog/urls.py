from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('create/', views.create_blog_post, name='create_post'),
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'), 
]