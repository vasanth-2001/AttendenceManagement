
from rest_framework.viewsets import ModelViewSet
from .models import Staff
from .serializers import StaffSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
class StaffViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
