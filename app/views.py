from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer,EmployeeSerializer
from .models import Employee, Student
# from logger import logger
import logging
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import UserSerializer
from .throttling import StudentThrottle
from rest_framework.throttling import AnonRateThrottle,ScopedRateThrottle
from rest_framework.generics import ListAPIView,ListCreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
import random
# Create your views here.



class TestStatus(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    throttle_classes = [StudentThrottle,AnonRateThrottle]
    def get(self,request):
        logging.debug('the debug')
        head_data = request.headers
        # print(head_data)
        data=request.data
        rn = data.get('rn')
        logger.info('----get record----')
        if rn:
            try:
                single_data = Student.objects.get(rn=rn)
                serializer = StudentSerializer(single_data)
                return Response(serializer.data,status=200)
            except Student.DoesNotExist:
                logger.error('record not found')
                return Response({'msg':'Id dose not found'},status=204)
        
        stu_data = Student.objects.all()
        serializer = StudentSerializer(stu_data,many=True)
        return Response(serializer.data,status=200)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data saved1'},status=201)
        else:
            return Response({'msg':serializer.errors},status=203)
        

    def put(self,request):
        student_data = request.data
        rn = student_data.get('rn')
        print(rn)
        try:
            student = Student.objects.get(rn=rn)
            serializer = StudentSerializer(student,data=student_data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data has updated!'},status=205)
            else:
                return Response({'msg':'Invalid data!'},status=203)
        except Student.DoesNotExist:
            return Response({'msg':'Rn not existed!'},status=204)

    def delete(self,request):
        data = request.data
        rn = data.get('rn')
        if rn:
            try:
                student = Student.objects.get(rn=rn).delete()
                return Response({'msg':'Student deleted!'},status=204)
            except Student.DoesNotExist:
                return Response({'msg':'Roll No does not exsited!'},status=204)
        return Response({'msg':'Please pass roll no'},status=206    )


class Logout(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        request.user.auth_token.delete()
        return Response({'msg':'Logout!'},status=status.HTTP_200_OK)

class SignUp(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self,request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'User created!'},status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)
        except Exception as e:
            return Response(e,status=500)

            


# Emplyee views

class EmployeeList(ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'emp_view'

class EmployeeCreate(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'emp_create'

class EmplyeeUpdate(UpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeDelete(DestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeRertive(RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()








