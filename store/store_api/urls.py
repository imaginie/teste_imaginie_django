# -*- coding: utf-8 -*-

from django.conf.urls import (url, include)
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash=False)
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
]
urlpatterns += router.urls
