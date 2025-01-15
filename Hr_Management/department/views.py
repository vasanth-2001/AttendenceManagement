
from rest_framework.viewsets import ModelViewSet
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
