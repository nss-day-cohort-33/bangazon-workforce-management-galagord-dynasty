from django.urls import path
from django.conf.urls import include
from hrapp import views
from django.contrib.auth import views as auth_views
from .views import *


app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('employee/form/', employee_form, name='employee_form'),
]
