from django.urls import path, include
from .views import *


urlpatterns = [
    path("", index, name='index'),
    path("delete/<int:id>", delete_card, name='delete_card')
]