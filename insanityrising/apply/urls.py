from django.conf.urls import url
from . import views

app_name = 'apply'

urlpatterns = [
    url(r'^apply/', views.apply, name='apply'),
]
