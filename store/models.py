from django.db import models

# Create your models here.


class Categories(models.Model):
    """
    Categories model
    """
    name = models.CharField(max_length=120)
    friendly_name = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.friendly_name}"


class Packs(models.Model):
    """ Packs model """
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(max_length=500)
    image = models.ImageField(null=False, blank=False, upload_to="images/")
    download_link = models.CharField(max_length=250, null=False, blank=False)
    demo_link = models.TextField(max_length=1000)
    stripe_price_id = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
