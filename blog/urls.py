from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('blog-list-gtm/', views.ThreadList.as_view(), name='thread'),
    path('about/', views.About, name='about'),
    path('blogs/', views.BlogList, name='blogs'),
    path('contact/', views.Contact, name='contact'),
    path('partners/', views.Partners, name='partners'),
    path('create_thread/', views.AddThread.as_view(), name="create_thread"),
    path('like/<slug:slug>', views.ThreadLike.as_view(), name='thread_like'),
    path('<slug:slug>/', views.ThreadDetail.as_view(), name="thread_detail")
]
