from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.files.storage import FileSystemStorage
# fs = FileSystemStorage(location="/media/images/")
class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Items(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.TextField()
    item_name = models.TextField(max_length=500 ,unique=True)
    item_description = models.TextField(max_length=1000)
    sku = models.IntegerField(
        validators=[MinValueValidator(1000000000), MaxValueValidator(2147483647) ], unique=True
    )
    original_price = models.FloatField()
    current_price = models.FloatField()
    discount_percentage = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    return_period = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.item_name


# class Rating(models.Model):
#     item_id = models.OneToOneField(Items, on_delete=models.CASCADE)

# class Product(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     description = models.TextField()
