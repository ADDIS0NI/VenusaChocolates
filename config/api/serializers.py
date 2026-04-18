from rest_framework import serializers
from .models import Chocolate, Ingredient, Media, Quote

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']


class MediaSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ['type', 'file']

    def get_file(self, obj):
        request = self.context.get('request')
        if obj.file:
            return request.build_absolute_uri(obj.file.url)
        return None


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['text']


class ChocolateSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    media = MediaSerializer(many=True, read_only=True)
    quote = QuoteSerializer(read_only=True)

    class Meta:
        model = Chocolate
        fields = [
            'id',
            'name',
            'description',
            'price',
            'rating',
            'origin',
            'ingredients',
            'media',
            'quote'
        ]