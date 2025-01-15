from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ApplicantViewSet

router =DefaultRouter()
router.register('',ApplicantViewSet,basename='applicant')

app_name='applicant'
urlpatterns = [
      path('',include(router.urls)),
]
