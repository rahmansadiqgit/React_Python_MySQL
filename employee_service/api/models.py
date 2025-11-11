from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.charField(max_length=100)
    department = models.charField(max_length=100)
    role = models.charField(max_length=100)

    def __str__(self):
      return self.name