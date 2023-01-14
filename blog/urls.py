from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('blogs/', views.BlogList, name='blogs'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register')
]
