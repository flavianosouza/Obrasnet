from django.urls import path

from obrasnet.views import *

urlpatterns = [
    path("", index, name='home'),

    path("signin/", signin, name='signin'),
    path("signout/", signout, name='signout'),
    path("register/", register, name='register'),

    path("requirements/", requirements, name='requirements'),
    path("design_recommendations", design_recommendations, name='design_recommendations'),
    path("scrap/", scrap_history, name='scrap_history'),
]