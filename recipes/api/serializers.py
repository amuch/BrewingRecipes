from rest_framework import serializers
from ..models import Style, Malt, MaltWeight, HopAcid, Hop, HopAddition, Yeast, Recipe

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ['name', 'description']

class MaltSerializer(serializers.ModelSerializer):
    class Meta:
        model = Malt
        fields = ['name', 'lovibond', 'description']

class HopAcidSerializer(serializers.ModelSerializer):
    class Meta:
        model = HopAcid
        fields = ['alpha_acid']

class HopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hop
        fields = ['name', 'alpha_acid', 'description']

class YeastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yeast
        fields = ['name', 'description']

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name',
            'style',
            'description',
            'batch_size',
            'boil_size',
            'original_gravity',
            'final_gravity',
            'mash_temperature',
            'unit',
            'special_instructions',
            'yeast']

class MaltWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaltWeight
        fields = ['malt', 'weight', 'unit', 'recipe']

class HopAdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HopAddition
        fields = ['hop', 'weight', 'unit', 'duration', 'recipe']
