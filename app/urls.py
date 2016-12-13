from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^a$', views.analysisA, name='A'),
    url(r'^b$', views.analysisB, name='B'),
]
