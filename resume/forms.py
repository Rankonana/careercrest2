from django import forms

class ResumeForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    professional_summary = forms.CharField(label='Professional Summary',max_length=100)
