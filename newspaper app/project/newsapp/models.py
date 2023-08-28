from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from typing import *


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profilepic = models.ImageField(null=True, default="images/default.jpg")


    def clean(self):
        super().clean()
        if self.date_of_birth and self.date_of_birth > date.today():
            raise ValidationError("Date of birth cannot be in the future.")

    def __str__(self): 
        return self.username 


class Category(models.Model):
    name = models.CharField(max_length=30)
    # article = models.ManyToManyField('Article', related_name="Articles")

    def __str__(self) -> str:
        return f"{self.name}"

    def to_dict(self) -> dict:
        return{
            'id':self.id,
            'name':self.name
        }


class Article(models.Model):
    title = models.TextField(null=True)
    publish_date = models.DateField(auto_now_add=True)
    article_body = models.TextField(null=True)
    category = models.ForeignKey(Category, related_name="Categories", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}, {self.publish_date}, {self.article_body}"  

    def to_dict(self) -> dict:
        return{
            'id':self.id,
            'title':self.title,
            'publishdate':self.publish_date,
            'articlebody':self.article_body,
            'category':self.category.id
        }

