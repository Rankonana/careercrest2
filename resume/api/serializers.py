from rest_framework.serializers import ModelSerializer
from resume.models import *



class SoftwareSerializer(ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'

class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'