from django.shortcuts import render
from .models import Applicant

def applicant_list(request):
    applicants = Applicant.objects.all()
    return render(request, 'applicant/applicant_list.html', {'applicants': applicants})
