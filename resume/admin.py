from django.contrib import admin

# Register your models here.

from .models import Resume,Education,WorkExperience,Skill
from .models import Summary,Accomplishments,Affiliations,AdditionalInformation,Software,Languages, Certifications, Interests,YourOwn


admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Skill)

admin.site.register(Summary)
admin.site.register(Accomplishments)
admin.site.register(Affiliations)
admin.site.register(AdditionalInformation)
admin.site.register(Software)
admin.site.register(Languages)
admin.site.register(Certifications)
admin.site.register(Interests)
admin.site.register(YourOwn)



