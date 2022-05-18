from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('home/', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('aboutus/', views.aboutus, name='aboutus'),
]