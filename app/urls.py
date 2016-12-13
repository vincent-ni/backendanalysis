from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^analysis_a$', views.analysisA, name='analysisA'),
    url(r'^analysis_b$', views.analysisB, name='analysisB'),
]
