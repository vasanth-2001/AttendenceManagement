from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Applicant
from .serializers import ApplicantSerializer
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from rest_framework.decorators import action
class ApplicantViewSet(ModelViewSet):
    queryset = Applicant.objects.all()
    # return render(request, 'applicant/applicant_list.html', {'applicants': applicants})
    serializer_class = ApplicantSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return ApplicantSerializer
        if self.action == 'create':
            return ApplicantSerializer
        return self.serializer_class
    
   
    #get all applicant

    def list(self,request):
        try:
            applicant_objs = Applicant.objects.all()
            serializer = self.get_serializer(applicant_objs, many = True)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #add applicant
    def create(self,request):
        try:
            serializer =self.get_serializer(data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_201_CREATED,
                'data': serializer.data,
                'messaage':'Applicant added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single applicant
    def retrieve(self,request,pk=None):
        try:
            id = pk
            if id is not None:

                #applicant_objs = Applicant.objects.all()
                applicant_objs = self.get_object()
                serializer = self.get_serializer(applicant_objs)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update all fields of aplicant
    def update(self,request, pk=None):
        try:
            #applicant_objs = Applicant.objects.all()
            applicant_objs = self.get_object()
            serializer = self.get_serializer(applicant_objs,data=request.data, partial=False)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage':'Applicant updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update specific fields

    def partial_update(self,request, pk=None):
        try:
            #applicant_objs = Applicant.objects.all()
            applicant_objs = self.get_object()
            serializer = self.get_serializer(applicant_objs,data=request.data,partial = True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage':'Applicant updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    def destroy(self, request,pk):
        try:
            id=pk
            applicant_obj = self.get_object()
            applicant_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage':'Applicant deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })