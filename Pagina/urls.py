from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('grade', views.grade, name='grade'),
    path('news', views.news, name='news'),
    path('downloads', views.downloads, name='downloads'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('actividades/<int:pk>/', views.acti, name='acti'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]