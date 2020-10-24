from django.urls import path
from django.contrib.auth import views as aunt_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', aunt_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),
    path('signup', views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
]