from django.urls import path
from .views import *

urlpatterns = [
    path("" ,home , name='home'),
    path('upadte<pk>', update, name='update'),
    path('delete<pk>', delete, name='delete')
]
