
from rest_framework.viewsets import ModelViewSet
from .models import Leave
from .serializers import LeaveSerializer

class LeaveViewSet(ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
