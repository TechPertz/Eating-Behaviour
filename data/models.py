from django.db import models
from users import models as users_models
from django.utils.html import mark_safe

# Create your models here.

class Image(models.Model):
    kid = models.ForeignKey(users_models.Kid, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    groups = models.CharField(max_length=255, choices=[('Veg','Veg',), ('Fruit','Fruit'), ('Grain','Grain'), ('Protein','Protein'), ('Dairy','Dairy'), ('Confectionary','Confectionary'), ('Unknown','Unknown')], default='Unknown')