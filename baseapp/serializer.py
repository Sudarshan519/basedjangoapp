from rest_framework import serializers
from . models import Contact
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Product
#         fields=('id',
#         'name','get_absolute_url',
#         'description',
#         'price',
#         'get_image',
#         'get_thumbnail')

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields="__all__"