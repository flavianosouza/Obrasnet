from django.urls import path

from core.views import *

urlpatterns = [
    path("", index, name='home'),

    path("signin/", signin, name='signin'),
    path("signout/", signout, name='signout'),
    path("singup/", signup, name='signup'),
    path("activate/<uid64>/<token>", activate, name='activate'),
]