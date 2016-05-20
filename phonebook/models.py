from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Phonebook(models.Model):
    name=models.CharField(max_length=30)
    mobile_number=PhoneNumberField()
    address=models.TextField()

    def __str__(self):
        return self.name
