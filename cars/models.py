from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.
class car(models.Model):
    carModel = models.CharField(max_length=64)
    year = models.DateField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.carModel