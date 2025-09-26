from django.contrib import admin
from django.urls import path,include
from .import views

from .views import FeedbackViewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'feedbacks',FeedbackViewSet)

urlpatterns=[

    path("",include(router.urls))

]