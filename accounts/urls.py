from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('user_logout/', views.user_logout, name='user_logout'),
]
