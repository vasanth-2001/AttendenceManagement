
from rest_framework.viewsets import ModelViewSet
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    
    
    def get_serializer_class(self):
        if self.action == 'list':
            return DepartmentSerializer
        if self.action == 'create':
            return DepartmentSerializer
        return self.serializer_class
    
   
    #get all departments

    def list(self,request):
        try:
            department_objs = Department.objects.all()
            serializer = self.get_serializer(department_objs, many = True)

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

    #add department
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
                'messaage':'Department added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single department
    def retrieve(self,request,pk=None):
        try:
            id = pk
            if id is not None:

                #department_objs = Department.objects.all()
                department_objs = self.get_object()
                serializer = self.get_serializer(department_objs)

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

    #update all fields of department
    def update(self,request, pk=None):
        try:
            #department_objs = Department.objects.all()
            department_objs = self.get_object()
            serializer = self.get_serializer(department_objs,data=request.data, partial=False)

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
                'messaage':'Department updated successfully'
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
            #department_objs = Department.objects.all()
            department_objs = self.get_object()
            serializer = self.get_serializer(department_objs,data=request.data,partial = True)

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
                'messaage':'Department updated successfully'
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
            department_obj = self.get_object()
            department_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage':'Department deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })
