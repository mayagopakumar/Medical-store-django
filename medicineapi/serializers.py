from rest_framework import serializers
from medicine.models import Medicines

class MedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicines
        fields = '__all__'