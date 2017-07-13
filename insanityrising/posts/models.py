from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    pub_date = models.DateField()
    content = models.TextField()
    images = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    def pub_date_nice(self):
        return self.pub_date.strftime('%b %d %Y')