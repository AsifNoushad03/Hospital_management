from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.booking, name='booking'),
    path('search', views.search, name='search'),
]