from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=120)
    friendly_name = models.CharField(max_length=120)

    def __str__(self):
        return self.friendly_name

class Packs(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(max_length=500)
    image = models.ImageField(null=False, blank=False, upload_to="uploads/products/")
    file = models.FileField(upload_to="uploads/files/")
    demo_link = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
