from django.db import models

class Department(models.Model):
    '''
    specific department information
    '''

    department = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def __str__(self):
        return f"{self.department} {self.budget}"

    def get_absolute_url(self):
        return reverse("Department", kwargs={"pk": self.pk})


