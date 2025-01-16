
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


from rest_framework_simplejwt import authentication
from django.urls import path, include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="HR Management",
      default_version='v1',
      description="API project HR management",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="vasanth@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   authentication_classes=(authentication.JWTAuthentication,),
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/applicant/",include('applicant.urls')),
    # path("",include('applicant.urls')),
    path("api/Attendance/",include('Attendance.urls')),
    path('api/department/', include('department.urls')),
    path('api/leave/', include('leave.urls')),
    path('api/staff/', include('staff.urls')),
    path('api/user/', include('user.urls')),
    path('api/userlogin/', include('userlogin.urls')),
    path('api/token/',swagger_auto_schema(methods=['post'],security=[])(TokenObtainPairView.as_view())),
    path('api/token/refresh/',swagger_auto_schema(methods=['post'],security=[])(TokenRefreshView.as_view())),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
# ]+ static(
#      settings.MEDIA_URL,
#      document_root=settings.MEDIA_ROOT
# )