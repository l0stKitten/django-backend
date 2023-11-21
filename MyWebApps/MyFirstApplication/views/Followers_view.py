from rest_framework import viewsets
from ..serializers.Followers_serializer import FollowSerializer
from ..models.Follow import Follow

# Create your views here.
class FollowersView(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()