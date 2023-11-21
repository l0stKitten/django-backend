from rest_framework import serializers
from ..models.UsersPreference import UsersPreference
from ..models.User import User
from ..models.Preference import Preference

class UsersPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersPreference
        fields = ['id', 'user_id', 'preference_id']
    
