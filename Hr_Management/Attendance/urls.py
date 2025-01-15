
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AttendanceViewSet

router =DefaultRouter()
router.register('',AttendanceViewSet,basename='attendance')

app_name='attendance'
urlpatterns = [
      path('',include(router.urls)),
]
