
from rest_framework.viewsets import ModelViewSet
from .models import Attendance
from .serializers import AttendanceSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]