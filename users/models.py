from django.db import models

# Create your models here.

class Kid(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    parent_phone = models.IntegerField()
    parent_email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name