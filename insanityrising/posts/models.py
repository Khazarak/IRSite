from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    pub_date = models.DateField()
    content = models.TextField()
    images = models.ImageField()