from django.db import models


class Employee(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Address = models.CharField(max_length=100)
    Phone = models.CharField(max_length=10)

    def __str__(self):
        return self.Name
