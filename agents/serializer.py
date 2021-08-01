from rest_framework import serializers

from agents.models import AgentsData


class AgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentsData
        fields = '__all__'