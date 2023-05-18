from django.urls import path

from obrasnet.views import *

urlpatterns = [
    path("", index),

    path("/login", login),
    path("/logout", logout),
    path("/register", register),

    path("requirements/", requirements),
    path("design_recommendations", design_recommendations),
    path("scrap/", scrap_history),
]