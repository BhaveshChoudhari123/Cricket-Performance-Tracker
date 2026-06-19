from django.db import models

# Create your models here.
player_image = models.ImageField(
    upload_to='players/',
    blank=True,
    null=True
)