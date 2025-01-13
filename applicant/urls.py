from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('applicants/', include('applicant.urls')),
    path('departments/', include('department.urls')),
]
