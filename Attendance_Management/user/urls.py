from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserSerializer

router =DefaultRouter()
router.register('',UserSerializer,basename='user')

app_name='user'
urlpatterns = [
      path('',include(router.urls)),
]
