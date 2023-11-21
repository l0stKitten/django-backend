from rest_framework import viewsets
from ..serializers.UsersPreference_serializer import UsersPreferenceSerializer
from ..models.UsersPreference import UsersPreference

# Create your views here.
class UserPreferenceView(viewsets.ModelViewSet):
    serializer_class = UsersPreferenceSerializer
    queryset = UsersPreference.objects.all()