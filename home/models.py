from django.db import models
from phone_field import PhoneField


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = PhoneField()
    comment = models.TextField(max_length=400)
    date = models.DateField()

    def __str__(self):
        return self.email
