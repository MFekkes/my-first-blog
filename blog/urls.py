# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 15:43:15 2016

@author: marte_000
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]