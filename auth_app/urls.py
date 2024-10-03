from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
  path('', views.home, name='home'),
  path('service/', views.service, name='services'),
  path('about/', views.about, name='aboutus'),
  path('contact/', views.contact, name='contactus'),
  path('register/',views.register_view,name= 'register'),
  path('login/',views.login_view,name= 'login'),
  path('logout/',views.logout_view,name= 'logout'),
  path('dashboard/',views.dashboard_view,name= 'dashboard'),
  path('settings/',views.settings,name='settings'),
  path('delete_account/', views.delete_account, name='delete_account'),
]