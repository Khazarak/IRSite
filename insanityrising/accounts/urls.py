from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.user_login, name='userlogin'),
    url(r'^signup/', views.signup, name='signup'),
]
