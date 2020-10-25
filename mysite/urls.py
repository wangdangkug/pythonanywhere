from django.contrib import admin
from django.urls import path, include
from myweb import views
from django.contrib.auth import views as aunt_views

urlpatterns = [
	path('', views.index , name='index'),
	path('polls/',include('polls.urls')),
	path('myweb/',include('myweb.urls')),
	#path('united/', view.united),
	path('admin/', admin.site.urls),
    path('login', aunt_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),
	path('signup', views.signup, name='signup'),
	path('logout',views.logout, name='logout'),
	path('movie', views.movie),
	path('insertmovie', views.insertmovie),
]
