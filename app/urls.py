from django.urls import path
from .views import *

urlpatterns = [
    path("" ,home , name='home'),
    path('update_todo/', update_todo, name='update_todo'),
    path('delete_todo/', delete_todo, name='delete_todo'),


