from django.urls import path
from .views import*

urlpatterns = [
    path ('', index, name = 'home'),
    path ('history', History.as_view(), name = 'history')
]