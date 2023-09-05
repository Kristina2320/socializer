from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:pk>/', views.Socialize.as_view(), name='user-detail'),
    path('post/', views.Socialize.as_view(), name='post-create'),
    path('post/<int:pk>/', views.Socialize.as_view(), name='post-detail'),
    path('comment/', views.Socialize.as_view(), name='comment-create'),
    path('user/register/', views.Socialize.as_view(), name='user-register'),
    path('user/login/', views.Socialize.as_view(), name='user-login'),
]