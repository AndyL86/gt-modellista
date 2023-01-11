from django.urls import path
from . import views


urlpatterns = [
    path('', views.ThreadList.as_view(), name='home'),
    path('about/', views.About, name='about'),
    path('blogs/', views.BlogList, name='blogs'),
]
