from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from random import randint
from authApp.models import id_generator
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

# Create your models here.

class Category(models.Model):
    id = models.CharField(default=id_generator, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# class AdsImage(models.Model):
#     image = models.ImageField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])])
#     ads = models.ForeignKey('ads.Ads', on_delete=models.CASCADE)

class Ads(models.Model):
    id = models.CharField(default=id_generator, primary_key=True)
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # image = models.ForeignKey('ads.AdsImage', on_delete=models.CASCADE)
    image = models.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg', 'heic', 'img'])],default='default_essay1.jpg')
    subject = models.CharField(max_length=150)
    publish_time = models.DateTimeField(default=timezone.now)
    bought = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=3, max_digits=10, default=0)

    class Meta:
        ordering = ['-publish_time']
    
    def __str__(self):
        return self.name


class Payment(models.Model):
    id = models.CharField(primary_key=True, default=id_generator)
    cc_number = CardNumberField('Card Number')
    cc_expiry = CardExpiryField('Expiration Date')
    cc_code = SecurityCodeField('CVV/CVC')
    

