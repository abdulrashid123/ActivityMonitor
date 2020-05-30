from django.conf.urls import url
from .views import *

urlpatterns = [

    url('^get_data/$', Activity.as_view(), name='path'),
]
