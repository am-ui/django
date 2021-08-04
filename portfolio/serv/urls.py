from edu.views import skill
from django import urls
from django.urls.conf import include
from django.urls import include, path
from . import views
from django.contrib import admin
urlpatterns=[
 path('services/', views.services, name='services')

]
