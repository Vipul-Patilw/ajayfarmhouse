
from django.urls import path,include
from .views import *

urlpatterns = [
   
    path('', Farm_land,name="farm_land")
]
