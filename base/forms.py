from django import forms
from .models import Job

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title','description','location',
                  'salary','jobType','jobCategory',
                  'importantInformation','expiryDate','applicationLinkOrEmail',
                  'companyname',
                  'companylogo']


