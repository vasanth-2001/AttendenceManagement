from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet

router =DefaultRouter()
router.register('',UserViewSet,basename='user')

app_name='user'
urlpatterns = [
      path('',include(router.urls)),
]
