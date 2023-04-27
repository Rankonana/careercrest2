from django.contrib.auth.models import User
from django.db import models

# class CustomUser(AbstractUser):
#     # Add custom fields here if needed
#     pass

class Resume(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    professional_summary = models.TextField()
    tracking = models.TextField()

    def __str__(self):
        return str(self.user.username) + " " + self.title

SOCIAL_CHOICES = (
    ('Twitter', 'LinkedIn'),
    ('Github', 'Website'),
    )
# class SocialLink(models.Model):
#     resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='SocialLink')
#     name = models.CharField(max_length=20,choices=SOCIAL_CHOICES,default='Twitter')
#     url = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    graduation_date = models.DateField()

    def __str__(self):
        return self.degree + " " +self.university

class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='work_experience')
    job_title = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    job_description = models.TextField()

    def __str__(self):
        return self.job_title + " " + self.employer

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)
    proficiency = models.CharField(max_length=255)

    def __str__(self):
        return self.skill_name
