from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.models import  TestModel
from app.serializers import TestSerializer

class TestViewset(ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
    
    def get_serializer_class(self,):
        if self.action == 'LIST':
            return TestSerializer
        return super().get_serializer_class()