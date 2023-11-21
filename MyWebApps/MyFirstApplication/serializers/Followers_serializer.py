from rest_framework import serializers
from ..models.Follow import Follow

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'user_id', 'seguidor', 'follow_type']