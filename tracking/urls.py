# tracking/urls.py
from django.urls import path
from .views import location_view

urlpatterns = [
    path('', location_view, name='home'),           # হোম পেজ
    path('location/', location_view, name='location'),
]