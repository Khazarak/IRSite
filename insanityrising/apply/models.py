from django.db import models
from django.core.mail import send_mail
from django.utils import timezone

APPLICATION_STATUS = (
    ('a', 'Accepted'),
    ('d', 'Declined'),
    ('u', 'Unchecked')
)
# Create your models here.
class Apply(models.Model):
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()
    applicant_age = models.IntegerField()
    applicant_favmmo = models.CharField(max_length=100)
    about_you = models.TextField()
    apply_date = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length=1, choices=APPLICATION_STATUS, default='u')

    def __str__(self):
        return self.applicant_name

    def send_conf_email(self, subject, message, fromEmail, toEmail):
        send_mail(subject,message,fromEmail,toEmail, fail_silently=False)
