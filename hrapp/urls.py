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
    path('training_programs/', training_programs_list, name='training_programs'),
    path('training_program_form/', training_program_form, name='program_form'),
    path('computers/', computer_list, name='computer_list'),
    path('computers/<int:computer_id>/', computer_details, name='computer_details'),
    path('departments/', department_list, name='department_list'),
]
