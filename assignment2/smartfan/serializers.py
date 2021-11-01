from rest_framework import serializers
from . models import fanStatus

class fanStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = fanStatus
        fields = '__all__'


