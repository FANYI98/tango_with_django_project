#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:39:34 2020

@author: yifan
"""

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('',views.index,name='index'),
]