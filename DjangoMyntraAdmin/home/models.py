from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Items(models.Model):
    image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.TextField()
    item_name = models.TextField()
    original_price = models.FloatField()
    current_price = models.FloatField()
    discount_percentage = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    return_period = models.IntegerField(),
    delivery_date = models.DateField(),

    def __str__(self):
        return self.content


# class Rating(models.Model):
#     item_id = models.OneToOneField(Items, on_delete=models.CASCADE)
