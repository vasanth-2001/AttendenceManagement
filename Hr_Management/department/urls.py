
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import DepartmentViewSet

router =DefaultRouter()
router.register('',DepartmentViewSet,basename='department')

app_name='department'
urlpatterns = [
      path('',include(router.urls)),
]
