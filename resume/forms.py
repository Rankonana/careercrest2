from django import forms

class ResumeForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    professional_summary = forms.CharField(label='Professional Summary',max_length=100)

class WorkForm(forms.Form):
    job_title = forms.CharField(label='job title',max_length=100)
    employer = forms.CharField(label='employer',max_length=100)
    start_date = forms.DateField(label='start date')
    end_date = forms.DateField(label='end date')
    job_description = forms.CharField(label='job description',max_length=100)