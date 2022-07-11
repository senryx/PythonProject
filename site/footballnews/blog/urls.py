from blog.views import *
from django.urls import path, re_path


urlpatterns = [
    path('home/', index),
    path('about/', about, name='about'),
    path('cats/<slug:cat>', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]