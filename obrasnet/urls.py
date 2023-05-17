from django.urls import path

from obrasnet.views import *

urlpatterns = [
    path("", index),
    path("requirements/", requirements),
    path("design_recommendations", design_recommendations),
]