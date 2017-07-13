from django.db import models

# Create your models here.
class Apply(models.Model):
    appName = models.CharField(max_length=100)
    appAge = models.IntegerField()
    appFavoriteMMO = models.CharField(max_length=100)
    aboutYou = models.TextField()

    def __str__(self):
        return self.appName


class ApplicantViewer(models.Model):
    appName = models.CharField(max_length=100)
    appAge = models.IntegerField()
    appFavoriteMMO = models.CharField(max_length=100)
    aboutYou = models.TextField()
    accepted = models.BooleanField()
    
    def onAccepted(self):
        return True