# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import *

from .views import like_set


urlpatterns = [
    url(r'^like/$', like_set, name="like_set"),
]