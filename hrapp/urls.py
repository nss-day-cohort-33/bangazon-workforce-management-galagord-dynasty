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
    path('employees/<int:employee_id>/', employee_details, name='employee'),
    path('training_programs/', training_programs_list, name='training_programs'),
    path('training_program_form/', training_program_form, name='program_form'),
    path('computers/', computer_list, name='computer_list'),
    path('computer/<int:computer_id>/', computer_details, name='computer_details'),
    path('computer/form', computer_form, name='computer_form'),
    path('departments/', department_list, name='department_list'),
]
