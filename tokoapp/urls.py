from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'tokoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('barang/<int:barang_id>', views.detail_barang, name='detail')
]