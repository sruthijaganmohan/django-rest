from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'admin',
            'active_years': 10
        }
        return Response(data)