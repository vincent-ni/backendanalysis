from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^a$', views.analysisA, name='analysisA'),
    url(r'^b$', views.analysisB, name='analysisB'),
]
