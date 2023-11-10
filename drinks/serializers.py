from rest_framework import serializers
from .models import Drinks

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        # id will be automatically added by django
        fields = ['id', 'name', 'description']