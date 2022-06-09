from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,AbstractUser
from django.core.validators import MinLengthValidator
from django.db.models.fields.related import ForeignKey




class MyUser(AbstractUser):
    phone = models.CharField(max_length=10,default="0000000000",validators=[MinLengthValidator(10)])
    
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELS = []

    def __str__(self):
        return self.username
    
# Create your models here.
class Expense(models.Model):
    item = models.CharField(max_length = 50)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField()
    userId = models.ForeignKey(MyUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.userId.username
