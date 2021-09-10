from django.urls import path
from .views import home

urlpatterns = [
    path('core/', home, name='core'),
]