from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Applicant
from .serializers import ApplicantSerializer

class ApplicantViewSet(ModelViewSet):
    queryset = Applicant.objects.all()
    # return render(request, 'applicant/applicant_list.html', {'applicants': applicants})
    serializer_class = ApplicantSerializer
