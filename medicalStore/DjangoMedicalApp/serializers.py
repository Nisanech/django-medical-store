from rest_framework import serializers

from DjangoMedicalApp.models import CompanyModel

# Obtener datos del modelo Company
'''
    El método serializers.HyperlinkedModelSerializer es un tipo específico de serializador que se utiliza cuando tienes 
    relaciones de clave externa (ForeignKey o OneToOneField) en tu modelo y deseas representar estas relaciones como 
    enlaces hipertextuales en lugar de datos anidados.
    
    El uso de HyperlinkedModelSerializer en lugar de ModelSerializer es útil cuando estás construyendo una API REST y 
    quieres proporcionar enlaces a otras vistas en lugar de datos anidados. Por ejemplo, en lugar de incrustar la 
    información completa de un objeto relacionado, simplemente proporcionarías un enlace a ese objeto, lo que puede 
    hacer que tu API sea más eficiente y fácil de usar para los clientes.
'''


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ["name", "licence_no", "address", "contact_no", "email", "description"]
