from django.db import models
from users import models as users_models

# Create your models here.

class Image(models.Model):
    kid = models.ForeignKey(users_models.Kid, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)