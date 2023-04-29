from django import forms

class ResumeForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100,required=False)
    image = forms.ImageField(required=False)
    # firstname = forms.CharField(label='firstname', max_length=100)
    lastname = forms.CharField(label='lastname', max_length=100,required=False)
    profession = forms.CharField(label='profession', max_length=100,required=False)
    city = forms.CharField(label='city', max_length=100,required=False)
    country = forms.CharField(label='country', max_length=100,required=False)
    postalcode = forms.CharField(label='postalcode', max_length=100,required=False)
    phone = forms.CharField(label='phone', max_length=100,required=False)
    email = forms.EmailField(label='email', max_length=100,required=False)
    professional_summary = forms.CharField(label='Professional Summary',max_length=100,required=False)

class WorkForm(forms.Form):
    job_title = forms.CharField(label='job title',max_length=100)
    employer = forms.CharField(label='employer',max_length=100)
    city = forms.CharField(label='city',max_length=100)
    country = forms.CharField(label='country',max_length=100)
    start_date = forms.DateField(label='start date')
    end_date = forms.DateField(label='end date')
    job_description = forms.CharField(label='job description',max_length=100)

class EduForm(forms.Form):
    schoolname = forms.CharField(label='School Name',max_length=100)
    schoollocation = forms.CharField(label='School Location',max_length=100)
    degree = forms.CharField(label='Degree',max_length=100)
    fieldofstudy = forms.CharField(label='Field of Study',max_length=100)
    start_date = forms.DateField(label='Start date')
    end_date = forms.DateField(label='End date')
    edu_description = forms.CharField(label='Description',max_length=100)