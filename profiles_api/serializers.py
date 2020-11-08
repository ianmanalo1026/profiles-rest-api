from rest_framework import serializers

class HellowSerializer(serializers.Serializer):
    """Serializes a name filed for testing our APIView"""
    name = serializers.CharField(max_length=10)