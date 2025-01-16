
from rest_framework.viewsets import ModelViewSet
from .models import Attendance
from .serializers import AttendanceSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return AttendanceSerializer
        if self.action == 'create':
            return AttendanceSerializer
        return self.serializer_class
    
   
    #get all attendance

    def list(self,request):
        try:
            attendance_objs = Attendance.objects.all()
            serializer = self.get_serializer(attendance_objs, many = True)

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

    #add attendance
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
                'messaage':'Attendance added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single attendance
    def retrieve(self,request,pk=None):
        try:
            id = pk
            if id is not None:

                #attendance_objs = Attendance.objects.all()
                attendance_objs = self.get_object()
                serializer = self.get_serializer(attendance_objs)

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
            #attendance_objs = Attendance.objects.all()
            attendance_objs = self.get_object()
            serializer = self.get_serializer(attendance_objs,data=request.data, partial=False)

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
                'messaage':'Attendance updated successfully'
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
            #attendance_objs = Attendance.objects.all()
            attendance_objs = self.get_object()
            serializer = self.get_serializer(attendance_objs,data=request.data,partial = True)

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
                'messaage':'Attendance updated successfully'
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