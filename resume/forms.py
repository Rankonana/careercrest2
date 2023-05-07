from django import forms
import datetime

class ResumeForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100,required=False,
                    widget=forms.TextInput(attrs={'placeholder': 'Title','class':'form-control'}))
    image = forms.ImageField(required=False)
    firstname = forms.CharField(label='First name',
                    widget=forms.TextInput(attrs={'placeholder': 'First name','class':'form-control'}), max_length=100,required=False)

    lastname = forms.CharField(label='Last name',
                    widget=forms.TextInput(attrs={'placeholder': 'Last name','class':'form-control'}), max_length=100,required=False)
    
    profession = forms.CharField(label='Profession',
                    widget=forms.TextInput(attrs={'placeholder': 'Profession','class':'form-control'}), max_length=100,required=False)
    city = forms.CharField(label='City',
                    widget=forms.TextInput(attrs={'placeholder': 'City','class':'form-control'}), max_length=100,required=False)
    country = forms.CharField(label='Country',
                    widget=forms.TextInput(attrs={'placeholder': 'Country','class':'form-control'}), max_length=100,required=False)
    postalcode = forms.CharField(label='Postalcode',
                    widget=forms.TextInput(attrs={'placeholder': 'Postal code','class':'form-control'}), max_length=100,required=False)
    phone = forms.CharField(label='Phone',
                    widget=forms.TextInput(attrs={'placeholder': 'Phone','class':'form-control'}), max_length=100,required=False)
    email = forms.EmailField(label='E-mail',
                    widget=forms.TextInput(attrs={'placeholder': 'E-mail','class':'form-control'}), max_length=100,required=False)
    professional_summary = forms.CharField(label='Professional Summary:',
                                           widget=forms.Textarea(attrs={'cols': 50, 'rows': 10,'placeholder': 'Write your summary here...','class':'form-control'}),required=False
                                           )

class ImageForm(forms.Form):
    image = forms.ImageField(required=False)


class SocialForm(forms.Form):
    name = forms.CharField(label='Site name',
                    widget=forms.TextInput(attrs={'placeholder': 'name','class':'form-control'}),max_length=100)
    url = forms.CharField(label='url',
                    widget=forms.TextInput(attrs={'placeholder': 'url','class':'form-control'}),max_length=100)   

    
class WorkForm(forms.Form):
    job_title = forms.CharField(label='Job Title',
                    widget=forms.TextInput(attrs={'placeholder': 'Job Title','class':'form-control'}),max_length=100)
    employer = forms.CharField(label='Employer',
                    widget=forms.TextInput(attrs={'placeholder': 'Employer','class':'form-control'}),max_length=100)
    city = forms.CharField(label='City',
                    widget=forms.TextInput(attrs={'placeholder': 'City','class':'form-control'}),
                    max_length=100)
    country = forms.CharField(label='Country',
                    widget=forms.TextInput(attrs={'placeholder': 'Country','class':'form-control'}),max_length=100)
    start_date = forms.DateField(label='Start date',
                    widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    end_date = forms.DateField(label='End date',
                    widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    job_description = forms.CharField(label='Job description:',
                                           widget=forms.Textarea(attrs={'cols': 50, 'rows': 10,'class': 'form-control','placeholder': 'Type in your achievements and responsibilities here.'})
                                           )

class EduForm(forms.Form):
    schoolname = forms.CharField(label='School Name',
                    widget=forms.TextInput(attrs={'placeholder': 'School Name','class':'form-control'}),
                    max_length=100)
    schoollocation = forms.CharField(label='School Location',
                    widget=forms.TextInput(attrs={'placeholder': 'School Location','class':'form-control'}),
                    max_length=100)
    degree = forms.CharField(label='Qualification',
                    widget=forms.TextInput(attrs={'placeholder': 'Qualification','class':'form-control'}),
                    max_length=100)
    fieldofstudy = forms.CharField(label='Field of Study',
                    widget=forms.TextInput(attrs={'placeholder': 'Field of Study','class':'form-control'}),
                    max_length=100)
    start_date = forms.DateField(label='Start date',
                    widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    end_date = forms.DateField(label='End date',
                    widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    edu_description = forms.CharField(label='Description:',
                                           widget=forms.Textarea(attrs={'cols': 50, 'rows': 10,'class': 'form-control','placeholder': 'Enter description here...'})
                                           )
    
class SkillForm(forms.Form):
    skill_name = forms.CharField(label='Skill',
                    widget=forms.TextInput(attrs={'placeholder': 'Skill','class':'form-control'}),max_length=100)
    proficiency = forms.CharField(label='Proficiency',
                    widget=forms.TextInput(attrs={'placeholder': 'Proficiency','class':'form-control'}),max_length=100)

class LanguageForm(forms.Form):
    language_name = forms.CharField(label='language',
                    widget=forms.TextInput(attrs={'placeholder': 'language','class':'form-control'}),max_length=100)
    proficiency = forms.CharField(label='Proficiency',
                    widget=forms.TextInput(attrs={'placeholder': 'Proficiency','class':'form-control'}),max_length=100)

class InterestForm(forms.Form):
    interest_name = forms.CharField(label='Interest',
                    widget=forms.TextInput(attrs={'placeholder': 'Add your interest...','class':'form-control'}),max_length=100)

class AccomplishmentForm(forms.Form):
    accomplishments = forms.CharField(label='Accomplishment',
                                      widget=forms.Textarea(attrs={'cols': 100, 'rows': 13,
                                                                   'placeholder': 'Write about your accomplishments here.',
                                                                   'class':'form-control'}),
                                      required=False,max_length=100)

class AffiliationForm(forms.Form):
    affiliations = forms.CharField(label='Affiliations: ',
                    widget=forms.Textarea(attrs={'cols': 100, 'rows': 13,'placeholder': 'Add your Affiliations here...','class':'form-control'}),max_length=100)
    

class AddsForm(forms.Form):
    additionalinformation = forms.CharField(label='Additional Information: ',
                                            widget=forms.Textarea(attrs={'cols': 100, 'rows': 13,'placeholder': 'Add your details here ...','class':'form-control'}),required=False
                                           ,max_length=100)

class SoftwareForm(forms.Form):
    software_name = forms.CharField(label='Software',
                    widget=forms.TextInput(attrs={'placeholder': 'Software','class':'form-control'}),max_length=100)
    proficiency = forms.CharField(label='proficiency',
                    widget=forms.TextInput(attrs={'placeholder': 'Proficiency','class':'form-control hidden'}),max_length=100)

class CertificationForm(forms.Form):
    certification_name = forms.CharField(label='Certification',
                    widget=forms.TextInput(attrs={'placeholder': 'Certification','class':'form-control'}),max_length=100)
    certification_date = forms.DateField(label='End date',
                    widget=forms.DateInput(attrs={'type': 'date','class':'form-control'}))

class YourownForm(forms.Form):
    yourown_name = forms.CharField(label='Your own: ',
                                           widget=forms.Textarea(attrs={'cols': 100, 'rows': 13,'placeholder': 'Your own','class':'form-control'}),required=False
                                           )

class SoftwareForm(forms.Form):
    software_name = forms.CharField(label='Software',
                    widget=forms.TextInput(attrs={'placeholder': 'Software','class':'form-control'}),max_length=100)
    proficiency = forms.CharField(label='Proficiency',
                    widget=forms.TextInput(attrs={'placeholder': 'Proficiency','class':'form-control'}),max_length=100)
