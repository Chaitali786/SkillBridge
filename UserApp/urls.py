# UserApp/urls.py
from django.urls import path
from . import views as user_views

urlpatterns = [
    path('', user_views.home, name='home'),
    path('register/', user_views.user_register, name='user_register'),
    path('login/', user_views.user_login, name='user_login'),
    path('logout/', user_views.user_logout, name='user_logout'),
]
