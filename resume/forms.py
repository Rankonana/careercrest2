from django.forms import ModelForm
from .models import Resume, WorkExperience, Education, Skill


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

class WorkExperienceForm(ModelForm):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

