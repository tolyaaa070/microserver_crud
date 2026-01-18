from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import OneToOneField
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    category_image = models.FileField(upload_to='category_icons/', null=True, blank=True)
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='sub_cat')
    subcat_name = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return f'{self.category} - {self.subcat_name}'

class Product(models.Model):
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE,related_name='sub_category_product')
    product_name = models.CharField(max_length=70)
    owner_id = models.SmallIntegerField()
    article_num= models.PositiveIntegerField(unique=True)
    description = models.TextField()
    product_type = models.BooleanField(default=False)
    product_video = models.FileField(upload_to='product_videos/',null=True, blank=True)
    price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_name}'

    def get_avg_rating(self):
        rating=self.product_reviews.all()
        if rating.exists():
            return round(sum([i.stars for i in rating]) / rating.count(),1)
        return 0
    def get_count_reviews(self):
        return self.product_reviews.count()
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_photos')
    product_image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f'{self.product}, {self.product_image}'

class Reviews(models.Model):
    user_id= models.SmallIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_reviews')
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1,6)])
    created = models.DateTimeField(auto_now_add=True)

