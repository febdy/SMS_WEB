from django.db import models

# Create your models here.


class StoreInfo(models.Model):
    store_name = models.CharField(max_length=200)
    latitude = models.DecimalField(decimal_places=2, max_digits=50)
    longitude = models.DecimalField(decimal_places=3, max_digits=50)

