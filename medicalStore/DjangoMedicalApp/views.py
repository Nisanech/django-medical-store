from django.shortcuts import render
from rest_framework import viewsets

from DjangoMedicalApp.models import CompanyModel
from DjangoMedicalApp.serializers import CompanySerializer

# Create your views here.
'''
    ModelViewSet proporciona implementaciones predeterminadas para las acciones CRUD (Crear, Leer, Actualizar, Eliminar) 
    en tu modelo, lo que significa que obtienes las operaciones estándar de creación, recuperación, actualización y 
    eliminación sin necesidad de escribir mucho código.
'''


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
