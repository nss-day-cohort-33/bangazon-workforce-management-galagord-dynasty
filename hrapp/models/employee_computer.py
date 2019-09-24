from django.db import models

class EmployeeComputer(models.Model):
    """
    Creates the join table for the many to many relationship between computers and employees
    assigned_date: The date the computer is assigned to employee.
    unassigned_date: The date the computer is unassigned to employee.
    Author: Joe Shep/Krystal Gates
    methods: none
    """

    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    computer = models.ForeignKey("Computer", on_delete=models.CASCADE)
    assigned_date = models.DateField()
    unassigned_date = models.DateField(null=True, blank=True, default=None)
