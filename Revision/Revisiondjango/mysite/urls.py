from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [

    path("gallery/",views.gallery,name="gallery"),
    path("upload/",views.upload_image,name="upload"),
    path('download/<int:pk>/', views.download_image, name='download_image'),


]

