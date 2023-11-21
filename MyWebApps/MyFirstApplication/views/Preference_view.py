from rest_framework import viewsets
from ..serializers.Preference_serializer import PreferenceSerializer
from ..models.Preference import Preference

# Create your views here.
class PreferenceView(viewsets.ModelViewSet):
    serializer_class = PreferenceSerializer
    queryset = Preference.objects.all()