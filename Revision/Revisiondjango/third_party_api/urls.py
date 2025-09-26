from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns=[

    path("",views.index,name="index"),
    path('api/coins/', views.crypto_data_api, name='crypto_data_api'),
]

    

