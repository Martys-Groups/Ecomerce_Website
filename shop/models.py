from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    Product_name = models.CharField(max_length=150)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50)
    Brand = models.CharField(max_length=50, default="Marty's Cart")
    price = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to="shop/images")
    pub_date = models.DateField()

    def __str__(self):
        return self.Product_name
    