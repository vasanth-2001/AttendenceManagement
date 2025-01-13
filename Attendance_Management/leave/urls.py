from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import LeaveViewSet

router =DefaultRouter()
router.register('',LeaveViewSet,basename='leave')

app_name='leave'
urlpatterns = [
      path('',include(router.urls)),
]
