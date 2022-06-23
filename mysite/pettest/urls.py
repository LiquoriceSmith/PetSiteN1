from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePettest.as_view(), name='home'),
    path('test/', test, name='test'),
]
