from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelsSerializers):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']