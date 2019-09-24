from django.db import models
# from .department import Department

class TrainingProgram(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()

    class Meta:
        verbose_name = ("Training_Program")
        verbose_name_plural = ("Training_Programs")

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("Training_program_detail", kwargs={"pk": self.pk})
