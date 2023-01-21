from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('blogs/', views.BlogList, name='blogs'),
    path('contact/', views.Contact, name='contact'),
    path('partners/', views.Partners, name='partners'),
    path('blog-list-gtm/', views.ThreadList.as_view(), name='thread'),
    path('my_threads/', views.UserThreads.as_view(), name='my_threads'),
    path('create_thread/', views.AddThread.as_view(), name='create_thread'),
    path(
        'edit_thread/<int:pk>', views.EditThread.as_view(), name='edit_thread'
        ),
    path('<slug:slug>/', views.ThreadDetail.as_view(), name='thread_detail'),
    path('like/<slug:slug>', views.ThreadLike.as_view(), name='thread_like')
]
