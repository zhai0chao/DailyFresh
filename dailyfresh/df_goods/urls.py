#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'df_goods'
urlpatterns=[
    url(r'^$',views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.goodlist),
    url(r'^(\d+)/$', views.detail),
]