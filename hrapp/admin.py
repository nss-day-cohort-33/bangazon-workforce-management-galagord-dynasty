from django.contrib import admin
from .models import Department
from hrapp.models import Computer
from hrapp.models import TrainingProgram


# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Computer)
admin.site.register(TrainingProgram)
admin.site.register(Department)
