from django.db import models

# Create your models here.
class Apply(models.Model):
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()
    applicant_age = models.IntegerField()
    applicant_favmmo = models.CharField(max_length=100)
    about_you = models.TextField()

    def __str__(self):
        return self.applicant_name


# class ApplicantViewer(models.Model):