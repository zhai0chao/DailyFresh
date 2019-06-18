from django.conf.urls import url
from . import views

name = 'df_order'
urlpatterns = [
    url(r'^$', views.order),
    url(r'^addorder/$', views.order_handle),
    url(r'^pay&(\d+)/$', views.pay),
]