from rest_framework import serializers
from .models import *

class TestSerializer(serializers.ModelSerializer):
    class Meta:
      model = TestModel
      depth = 1
      fields = '__all__'