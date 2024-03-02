from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from djangorfapp.serializers import StudentSerializer
from djangorfapp.models import Student
from rest_framework.permissions import IsAuthenticated
# 16a48cc02d78b32d4328d215ccae4812e2a9baaf


class TestView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        # serializer = StudentSerializer(qs, many=True)
        student1 = qs.first()
        serializer = StudentSerializer(student1)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)