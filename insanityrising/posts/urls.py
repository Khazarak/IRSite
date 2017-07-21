from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_details, name='post_details'),
]