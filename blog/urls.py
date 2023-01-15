from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('blog-list-gtm/', views.ThreadList.as_view(), name='thread'),
    path('about/', views.About, name='about'),
    path('blogs/', views.BlogList, name='blogs'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('contact/', views.Contact, name='contact'),
    path('<slug:slug>/', views.ThreadDetail.as_view(), name="thread_detail")
]
