from django.urls import path
from . import views

urlpatterns = [
    path('loggy/', views.my_views, name='loggy'),
]
