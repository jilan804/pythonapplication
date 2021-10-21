from django.urls import path
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.uploadCsvView, name='index'),
    path('upload/csv', views.uploadCsv, name='upload_csv'),
]
