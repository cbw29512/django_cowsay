from django.db import models


# Create your models here.
class CowInput(models.Model):
    cow_input = models.TextField()

    def __str__(self):
        return self.cow_input
