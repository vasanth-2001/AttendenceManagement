from rest_framework import serializers
from .models import Applicant

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Applicant
        fields="__all__"
        read_only_field=['id'] 