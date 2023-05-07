from rest_framework.serializers import ModelSerializer
from resume.models import Software



class SoftwareSerializer(ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'