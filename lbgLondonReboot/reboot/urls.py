from django.conf.urls import url
from reboot import views
urlpatterns = [
url(r'^$', views.index, name='index'),
]