
from rest_framework.viewsets import ModelViewSet
from .models import Leave
from .serializers import LeaveSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
class LeaveViewSet(ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
