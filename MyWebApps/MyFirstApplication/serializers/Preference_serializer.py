from rest_framework import serializers
from ..models.Preference import Preference

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = '__all__'