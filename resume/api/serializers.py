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

class CertificationSerializer(ModelSerializer):
    class Meta:
        model = Certifications
        fields = '__all__'

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Resume
        fields = ['image','tracking']