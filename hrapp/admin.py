from django.contrib import admin
from .models import Department
from hrapp.models import Computer
from hrapp.models import TrainingProgram


# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Computer)
<<<<<<< HEAD
admin.site.register(TrainingProgram)
=======
admin.site.register(Department)
>>>>>>> a975786ba68a49b54c86f7838a4b5fd9c01f86e4
