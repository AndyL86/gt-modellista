from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('partners/', views.Partners, name='partners'),
    path('featured/', views.Featured.as_view(), name='featured'),
    path('blog_lists/', views.ThreadList.as_view(), name='blog_lists'),
    path('my_threads/', views.UserThreads.as_view(), name='my_threads'),
    path('create_thread/', views.AddThread.as_view(), name='create_thread'),
    path(
        'edit_thread/<int:pk>', views.EditThread.as_view(), name='edit_thread'
        ),
    path('delete_thread/<int:pk>/',
         views.delete_thread, name='delete_thread'),
    path('<slug:slug>/', views.ThreadDetail.as_view(), name='thread_detail'),
    path('like/<slug:slug>', views.ThreadLike.as_view(), name='thread_like')
]
