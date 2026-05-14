# serializers.py

from rest_framework import serializers


class ProductSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField(
        allow_blank=True,
        allow_null=True
    )
    price = serializers.IntegerField()
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField()