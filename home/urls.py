from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.Home),
    path('FindJob',views.FindJob, name='page2'),
    path('login',views.Login, name='login'),
    path('register',views.Register, name='register'),
    path('AddJob',views.AddJob, name='AddJob'),
    path('myjob',views.Myjob, name='Myjob'),
    # path('/index', Index),    .
    path('CompRegister',views.CompRegister, name='CompRegister'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]