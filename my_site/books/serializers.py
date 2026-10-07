from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_year(self, value):
        if value < 1970 or value > 2100:
            raise serializers.ValidationError("Year must be between 1970 and 2100.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value
