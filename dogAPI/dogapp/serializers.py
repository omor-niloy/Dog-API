from rest_framework import serializers
from dogapp.models import Dog , Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']


class DogSerializer(serializers.ModelSerializer):
    """breed = serializers.PrimaryKeyRelatedField(many=True, read_only=True)"""
    class Meta:
        model = Dog
        fields = ['name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy']
