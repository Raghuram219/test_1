from django.urls import path
from app.views import TestViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('testviewset',TestViewset,basename='testname')

urlpatterns = [

]

urlpatterns += router.urls