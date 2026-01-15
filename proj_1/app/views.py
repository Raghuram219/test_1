from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.models import  TestModel
from app.serializers import TestSerializer
from rest_framework.response import Response

class TestViewset(ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
    
    def get_serializer_class(self):
        if self.action == 'LIST':
            return TestSerializer
        return super().get_serializer_class()
    
    def list(self,request):
        print("==1==")
        qs= self.get_queryset()
        print("==2==")
        serializer= self.get_serializer(qs,many=True)
        if serializer.is_valid():
            data = serializer.data
        print("==4==")
        return Response(data)
    