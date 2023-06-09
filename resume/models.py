from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.db import models
from django.db import models
from django import forms


# class CustomUser(AbstractUser):
#     # Add custom fields here if needed
#     pass
class Resume(models.Model):
    user = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(default="NoImageBlue.png",null=True,blank=True)
    firstname = models.CharField(max_length=200,null=True,blank=True)
    lastname = models.CharField(max_length=200,null=True,blank=True)
    profession = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    country = models.CharField(max_length=200,null=True,blank=True)
    postalcode = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    professional_summary = models.TextField(null=True, blank=True)
    tracking = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.tracking

class SocialLinks(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='SocialLinks')
    name = models.CharField(max_length=200,null=True,blank=True)
    url = models.CharField(max_length=200,null=True,blank=True)
    socialtracking = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.socialtracking
class MonthYearField(models.DateField):
    def __init__(self, *args, **kwargs):
        kwargs['null'] = True
        kwargs['blank'] = True
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return value.strftime('%Y-%m')

    def to_python(self, value):
        if isinstance(value, str):
            return value
        if value is None:
            return value
        return value.strftime('%Y-%m')

    def get_prep_value(self, value):
        if value is None:
            return value
        return f'{value}-01'

    def formfield(self, **kwargs):
        defaults = {
            'form_class': MonthYearFieldForm,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)


class MonthYearFieldForm(forms.DateField):
    def to_python(self, value):
        if isinstance(value, str) and value == '':
            return None
        return super().to_python(value)


class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='work_experience')
    job_title = models.CharField(max_length=200,null=True,blank=True)
    employer = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    country = models.CharField(max_length=200,null=True,blank=True)
    start_date = MonthYearField()
    end_date = MonthYearField()
    job_description = models.TextField(null=True, blank=True)
    worktracking = models.CharField(max_length=200,null=True,blank=True)


    def __str__(self):
        return self.worktracking
    
class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education')
    schoolname = models.CharField(max_length=200,null=True,blank=True)
    schoollocation= models.CharField(max_length=200,null=True,blank=True)
    degree = models.CharField(max_length=200,null=True,blank=True)
    fieldofstudy = models.CharField(max_length=200,null=True,blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    edu_description = models.TextField(null=True, blank=True)
    edutracking = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.degree

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skill')
    skill_name = models.CharField(max_length=200,null=True,blank=True)
    proficiency = models.CharField(max_length=200,null=True,blank=True)
    skilltracking = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.skill_name

class Summary(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='summary')
    Summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Summary

class Accomplishments(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='accomplishment')
    accomplishments = models.CharField(max_length=200,null=True,blank=True)
    accomplishmenttracking = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.accomplishments
    
class Affiliations(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='affiliation')
    affiliations = models.CharField(max_length=200,null=True,blank=True)
    affiliationtracking = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.affiliations
    
class AdditionalInformation(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='additionalinformation')
    additionalinformation = models.TextField(null=True, blank=True)
    additionalinfotracking = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.additionalinformation
    
class Software(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,related_name='software')
    software_name = models.CharField(max_length=200,null=True,blank=True)
    proficiency = models.CharField(max_length=200,null=True,blank=True)
    softwaretracking = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.software_name
     
class Languages(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE ,related_name='language')
    language_name = models.CharField(max_length=200,null=True,blank=True)
    proficiency = models.CharField(max_length=200,null=True,blank=True)
    languagetracking = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.language_name

class Certifications(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,related_name='certification')
    certification_name = models.CharField(max_length=200,null=True,blank=True)
    certification_date = models.DateField(max_length=200,null=True,blank=True)
    certificationtracking = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.certificationtracking

class Interests(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,related_name='interest')
    interest_name = models.CharField(max_length=200,null=True,blank=True)
    interesttracking = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.interest_name

class YourOwn(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,related_name='yourown')
    yourown_name = models.TextField(null=True, blank=True)
    yourowntracking = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.yourown_name
