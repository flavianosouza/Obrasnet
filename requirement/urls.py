from django.urls import path

from requirement.views import *

urlpatterns = [
    path("", requirements, name='requirements'),
]